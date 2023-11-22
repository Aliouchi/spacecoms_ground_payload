from flask import Flask, jsonify, request
import requests
from logic_checks import *
from spacecraft_telem import *
from TestingPostman import *
app = Flask(__name__)

spacecraft = Spacecraft(identifier='ISS',latitude=2.55,longitude=5.66) #TBD
db_URL = 'http://example.com/post/add_request' 
M7URL = 'http://example.com/post/status'
M5URL = 'http://example.com/post/receive'
M7ImagesURL = 'http://example.com/payloadimage'

@app.route('/request', methods=['POST'])
def postRequestEndpoint():

    try:
        data = request.json  # Retrieve JSON data from the request body
      
        ID = request.args.get('ID')
        Longitude = float(request.args.get('Longitude'))
        Latitude = float(request.args.get('Latitude'))
        NumberOfImages = int(request.args.get('NumberOfImages'))

        # Check if any of the parameters are missing
        if None in [ID, Longitude, Latitude, NumberOfImages]:
            return jsonify({"message": "Missing one or more required parameters"}), 400

        #Save the current request data to MongoDB
        
        collection_file = "PostmanCollection.json"
        postMan_testResult = run_postman_tests(collection_file)
       
        if postMan_testResult:
            final_result = total_check(data,spacecraft)
            if final_result:
                status_code = 0
            else:
                status_code=1
        else:
            status_code=2
        
        response_data = {
            "ID": ID,
            "Longitude": Longitude,
            "Latitude": Latitude,
            "NumberOfImages": NumberOfImages, 
            "StatusCode": status_code
            
        }
        req = requests.post(db_URL,json=response_data)
       
     
            
        requests.post(M7URL,json=status_code)
        if status_code ==0: 
            requests.post(M5URL, json=data)
            return jsonify({"message": "Valid Request"})
        else: 
               return jsonify({"message": "Invalid Request"}), 400
           
    except Exception as e:
        return jsonify({"message": "Error processing the request"}), 400



@app.route('/images', methods=['POST'])
def postImagesEndpoint():
    try:
        data = request.json

        forward_response = requests.post(M7ImagesURL, json=data)
        forward_response.raise_for_status()

        return jsonify({"message": "Images processed successfully"}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"message": f"Error processing images: {str(e)}"}), 500
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)