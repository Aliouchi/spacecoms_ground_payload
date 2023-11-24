"""
This module contains the Flask application for handling requests and images.
"""

from __future__ import annotations

import requests
from flask import Flask, g, jsonify, request

from logic_checks import total_check
from request_struct import Request
from spacecraft_telem import Spacecraft
from TestingPostman import run_postman_tests

app = Flask(__name__)

DB_URL = 'http://example.com/post/add_request'
M7_URL = 'http://example.com/post/status'
M5_URL = 'http://example.com/post/receive'
M7_IMAGES_URL = 'http://example.com/payloadimage'

spacecraft = Spacecraft(identifier='ISS', latitude=2.55, longitude=5.66)  # TBD
@app.route('/receive', methods=['POST'])
def telemetry_endpoint():
    try:
        data = request.json

        identifier = data.get('ID')
        longitude = data.get('Longitude')
        latitude = data.get('Latitude')

        if None in [identifier, longitude, latitude]:
            return jsonify({"message": "Missing one or more required parameters"}), 400

        spacecraft_instance = Spacecraft(identifier, float(longitude), float(latitude))

        # Store the spacecraft instance in the global context variable 'g'
        g.spacecraft_instance = spacecraft_instance

        return jsonify({"message": "Telemetry data received successfully"}), 200


    except Exception as e:
        return jsonify({"message": f"Error processing telemetry data: {str(e)}"}), 400
@app.route('/request', methods=['POST'])
def post_request_endpoint():
    """
    Handle the '/request' endpoint for processing requests.
    """
    try:
        data = request.json  # Retrieve JSON data from the request body

        identifier = data.get('ID')
        longitude = data.get('Longitude')
        latitude = data.get('Latitude')
        number_of_images = data.get('NumberOfImages')
        longitude = float(longitude)
        latitude = float(latitude)
        number_of_images = int(number_of_images)
        status_code = -1
        # Check if any of the parameters are missing
        if None in [identifier, longitude, latitude, number_of_images]:
            status_code = 2
            #return jsonify({"message": "Missing one or more required parameters"}), 400

        # Save the current request data to MongoDB
        # collection_file = "PostmanCollection.json"
        # postman_test_result = run_postman_tests(collection_file)
        #postman_test_result = True
        # if postman_test_result:

        if status_code !=2:
            request_data = Request(identifier,longitude,latitude,number_of_images)
            final_result = total_check(request_data, spacecraft)
            if final_result:
                status_code = 0
            else:
                status_code =1


        response_data = {
            "ID": identifier,
            "Longitude": longitude,
            "Latitude": latitude,
            "NumberOfImages": number_of_images,
            "StatusCode": status_code
        }

        requests.post(DB_URL, json=response_data,timeout=500)




        # if requests.post('https://eon9k7ryz3jzzbf.m.pipedream.net', json=status_code,timeout=500):
        #     return jsonify({"message": "Status_code sent successfully", "status_code": status_code}), 200

    #     if status_code == 0:
    #         requests.post('https://eo97tu4xhnko5q3.m.pipedream.net', json=data,timeout=500)
    #         return jsonify({"message": "Valid Request"}), 200
    #     elif status_code==1:
    #         return jsonify({"message": "Rejected by logic"}),200
    #     elif status_code ==2:
    #         return jsonify({"message":"Rejected by Structure"}),200
    #     return jsonify({"message": "Invalid Request"}), 400

    except Exception as e:
        return jsonify({"message": f"Error processing the request: {str(e)}"}), 400

# @app.route('/images', methods=['POST'])
# def post_images_endpoint():
#     """
#     Handle the '/images' endpoint for processing images.
#     """
#     try:
#         data = request.json

#         forward_response = requests.post(M7_IMAGES_URL, json=data, timeout=500)
#         forward_response.raise_for_status()

#         return jsonify({"message": "Images processed successfully"}), 200

#     except requests.exceptions.RequestException as e:
#         return jsonify({"message": f"Error processing images: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
