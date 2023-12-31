"""
This module contains the Flask application for handling requests and images.
"""

from __future__ import annotations

import requests
from flask import Flask, jsonify, request

from app import ImageRequest
from logic_checks import total_check
from request_struct import Request
from spacecraft_telem import Spacecraft

# from TestingPostman import run_postman_tests

app = Flask(__name__)

FILE_NAME = "ServiceIPs.txt"

def load_ip(module_number, file_name):
    """ A method to get an IP address for the corresponding module from .txt file """
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            ip, service_number = line.strip().split(',')
            service_number = int(service_number)
            if service_number == module_number:
                return ip

DB_URL = 'http://127.0.0.1:5000'
M5_URL = load_ip(5, FILE_NAME) + ":8080"
M7_URL = load_ip(7, FILE_NAME) + ":8080"


spacecraft = Spacecraft(identifier='ISS', latitude=5.66, longitude=2.55)

@app.route('/request', methods=['POST'])
def post_request_endpoint():
    """ Handle the '/request' endpoint for processing requests. """
    try:
        data = request.json  # Retrieve JSON data from the request body

        # Parse Request contents to string variables
        identifier = data.get('ID')
        longitude = data.get('Longitude')
        latitude = data.get('Latitude')

        # Parse the strings parsed from the Request into the required datatypes
        longitude = float(longitude)
        latitude = float(latitude)

        status_code = -1
        # Check if any of the parameters are missing
        if None in [identifier, longitude, latitude]:
            status_code = 2

        # TODO: Need to run postman tests here. Objective for Sprint #4
        # collection_file = "PostmanCollection.json"
        # postman_test_result = run_postman_tests(collection_file)
        # if postman_test_result:

        if status_code !=2:
            request_data = Request(identifier,longitude,latitude)
            final_result = total_check(request_data, spacecraft)
            if final_result:
                status_code = 0
            else:
                status_code = 1

        # Saving the record to the database
        im_req = ImageRequest(identifier, longitude, latitude, status_code)
        requests.post(DB_URL + "/add_request", json=im_req.__dict__, timeout = 500)

        # Returning the status code to Module #7
        status_response = {
            "ID" : identifier,
            "Status" : status_code
        }
        requests.post(M7_URL + "/Status", json=status_response, timeout = 500)

        # Forming the request response to return to Module #7
        if status_code == 0:
            requests.post(M5_URL + "/receive", json = data, timeout = 500)
            return jsonify({"message": "Valid Request"}), 200
        elif status_code == 1:
            return jsonify({"message": "Rejected by logic"}),200
        elif status_code == 2:
            return jsonify({"message":"Rejected by Structure"}),200
        return jsonify({"message": "Invalid Request"}), 400

    except Exception as e:
        return jsonify({"message": f"Error processing the request: {str(e)}"}), 400

@app.route('/images', methods=['POST'])
def post_images_endpoint():
    """
    Handle the '/images' endpoint for processing images.
    """
    try:
        data = request.json

        requests.post(M7_URL + "/images", json=data, timeout=500)
       # forward_response.raise_for_status()

        return jsonify({"message": "Images processed successfully"}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"message": f"Error processing images: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
