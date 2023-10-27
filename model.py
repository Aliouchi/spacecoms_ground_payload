from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/endpoint', methods=['GET'])
def test_endpoint():
    try:
        action = request.args.get('action')
        location = request.args.get('location')
        number_of_images = request.args.get('number_of_images')  # Corrected parameter name
        capture_time = request.args.get('capture_time')  # Corrected parameter name

        # Check if any of the parameters are missing
        if None in [action, location, number_of_images, capture_time]:
            return jsonify({"message": "Missing one or more required parameters"}), 400

        response_data = {
            "action": action,
            "location": location,
            "number_of_images": number_of_images,
            "capture_time": capture_time
        }

        return jsonify(response_data)

    except Exception as e:
        return jsonify({"message": "Error processing the request"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)
