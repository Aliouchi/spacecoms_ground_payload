from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/endpoint', methods=['GET'])
def test_endpoint():
    try:
        ID = request.args.get('ID')
        Timeframe = int(request.args.get('Timeframe'))  # Convert to int
        Longitude = float(request.args.get('Longitude'))  # Convert to float
        Latitude = float(request.args.get('Latitude'))  # Convert to float
        NumberOfImages = int(request.args.get('NumberOfImages'))  # Convert to int

        # Check if any of the parameters are missing
        if None in [ID, Timeframe, Longitude, Latitude, NumberOfImages]:
            return jsonify({"message": "Missing one or more required parameters"}), 400

        response_data = {
            "ID": ID,
            "Timeframe": Timeframe,
            "Longitude": Longitude,
            "Latitude": Latitude,
            "NumberOfImages": NumberOfImages
        }

        return jsonify(response_data)

    except Exception as e:
        return jsonify({"message": "Error processing the request"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)