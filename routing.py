from flask import Flask, request, jsonify
import requests 
from app import Request

app = Flask(__name__)

sampleRequest = Request()
CandDH_URL = "https://example.com/other_module_endpoint"
ScientificOps_URL = "https://example.com/other_module_endpoint"

previousRequestContent = None

@app.route('/post/request', methods=['POST'])
def postRequestEndpoint():
    global previousRequestContent  

    try:
        ID = request.args.get('ID')
        Longitude = float(request.args.get('Longitude'))
        Latitude = float(request.args.get('Latitude'))
        NumberOfImages = int(request.args.get('NumberOfImages'))

        # Check if any of the parameters are missing
        if None in [ID, Longitude, Latitude, NumberOfImages]:
            return jsonify({"message": "Missing one or more required parameters"}), 400

        response_data = {
            "ID": ID,
            "Longitude": Longitude,
            "Latitude": Latitude,
            "NumberOfImages": NumberOfImages
        }

        if response_data == previousRequestContent:
            print("Duplicate Request Encountered! Discarded!")
            return jsonify({"message": "Duplicate Request"}), 400

        previousRequestContent = response_data

        finalResult = sampleRequest.total_check()
        if finalResult:
            response = postEndpoint(response_data)
        else:
            return jsonify({"message": "Invalid Incoming Request, Checks Failed!"}), 400

        return jsonify(response_data)

    except Exception as e:
        return jsonify({"message": "Error processing the request"}), 400

@app.route('/post/images', methods=['POST'])
def postImagesEndpoint():
    try:
        response_data = request.get_json()

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(ScientificOps_URL, json=response_data, headers=headers)  

        if response.status_code == 200:
            return jsonify({"message": "Response forwarded to Module A successfully"}), 200
        else:
            return jsonify({"message": "Failed to forward response to Module A"}), 500

    except Exception as e:
        return jsonify({"message": "Error Forwarding the Data Packet"}), 400

def postEndpoint(dataPacket):
    try:
        response = requests.post(CandDH_URL, json=dataPacket) 

        if response.status_code == 200:
            return jsonify({"message": "Request Forwarded Successfully"})
        else:
            return jsonify({"message": "Error Forwarding the Data Packet"}), 400

    except Exception as e:
        return jsonify({"message": "Error Forwarding the Data Packet"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)
