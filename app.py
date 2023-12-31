"""run flask and the database"""
from __future__ import annotations

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

# ImageRequest structure

class ImageRequest:
    """class structure for the image request"""
    def __init__(self, identifier, latitude, longitude, status):
        self.identifier = identifier
        self.latitude = latitude
        self.longitude = longitude
        self.status = status

def create_app():
    """this module will setup flask in addition to Mongo db database"""
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/payloadOpsDb"

    mongo = PyMongo(app)

    @app.route('/add_request', methods=['POST'])

    def add_request():
        """route that adds a new request with the specified structure to the database"""
        data = request.json
        mongo.db.requests.insert_one(data)
        return jsonify({'message': 'Request added successfully'})
# get request by id
    @app.route('/get_requests')
    def get_requests():
        """route that get all requests from the database"""
        requests = mongo.db.requests.find()
        request_list = []
        for req in requests:
            req['_id'] = str(req['_id'])
            request_list.append(req)
        return jsonify(request_list)

# get a specific request
    @app.route('/get_request', methods=['GET'])
    def get_request():
        """route to get a specific request by its id"""
        custom_id = request.headers.get('Identifier')

        if not custom_id:
            return jsonify({'error': 'No identifier provided'}), 400

        requests_cursor = mongo.db.requests.find({'identifier': custom_id})
        requests_list = list(requests_cursor)

        if requests_list:
            for request_data in requests_list:
                request_data['_id'] = str(request_data['_id'])
            return jsonify(requests_list)
        else:
            return jsonify({'error': 'No request found with the provided identifier'}), 404

# update requestt status
    @app.route('/update_status', methods=['POST'])
    def update_status():
        """route to update the status of a request"""
        data = request.json
        custom_id = data.get('identifier')
        new_status = data.get('status')


        if new_status not in [0, 1, 2, 3]:
            return jsonify({'error': 'Invalid status'}), 400

        result = mongo.db.requests.update_one(
        {'identifier': custom_id},
        {'$set': {'status': new_status}}
        )

        if result.modified_count:
            return jsonify({'message': 'Status updated successfully'})
        else:
            return jsonify({'error': 'No request found with the provided identifier'}), 404

#delete a request
    @app.route('/delete_request', methods=['DELETE'])
    def delete_request():
        """route to delete a request using a custom identifier"""
        data = request.json
        custom_id = data.get('identifier')

        result = mongo.db.requests.delete_one({'identifier': custom_id})

        if result.deleted_count:
            return jsonify({'message': 'Request deleted successfully'})
        else:
            return jsonify({'error': 'No request found with the provided identifier'}), 404

#check for duplicate requests
    @app.route('/check_duplicate', methods=['GET'])
    def check_duplicate():
        """Route to check if a request with the given identifier already exists"""
        identifier = request.headers.get('Identifier')

        if not identifier:
            return jsonify({'error': 'No identifier provided'}), 400

        existing_request = mongo.db.requests.find_one({'identifier': identifier})

        if existing_request:
            return jsonify({'duplicate': True,
                            'message': 'A request with this identifier already exists'})
        else:
            return jsonify({'duplicate': False,
                            'message': 'No duplicate request found'})

    return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)
