from flask import Flask, jsonify, request
import requests
from logic_checks import *
from spacecraft_telem import *
from TestingPostman import *
app = Flask(__name__)

spacecraft = Spacecraft()
db_URL = 'http://example.com/post/add_request'
M7URL = 'http://example.com/post/status'
M5URL = 'http://example.com/post/receive'


# Your MongoDB setup goes here

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


# @app.route('/post/images', methods=['POST'])
# def postImagesEndpoint():
#     try:
#         response_data = request.get_json()

#         headers = {
#             "Content-Type": "application/json"
#         }

#         response = requests.post(ScientificOps_URL, json=response_data, headers=headers)  

#         if response.status_code == 200:
#             return jsonify({"message": "Response forwarded to Module A successfully"}), 200
#         else:
#             return jsonify({"message": "Failed to forward response to Module A"}), 500

#     except Exception as e:
#         return jsonify({"message": "Error Forwarding the Data Packet"}), 400

# def postEndpoint(dataPacket):
#     try:
#         response = requests.post(CandDH_URL, json=dataPacket) 

#         if response.status_code == 200:
#             return jsonify({"message": "Request Forwarded Successfully"})
#         else:
#             return jsonify({"message": "Error Forwarding the Data Packet"}), 400

#     except Exception as e:
#         return jsonify({"message": "Error Forwarding the Data Packet"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)