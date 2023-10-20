"""Running Flask Server"""

from __future__ import annotations

from flask import Flask


class Request:
    """Request object - a local definition of the request structure"""
    id = "20231019_233715"
    longitude = 0.00
    latitude = 0.00
    number_of_images = 0

    def __init__(self, id, longitude, latitude, number_of_images):
        """A method to initialize the Request class"""
        self.id = id
        self.longitude = longitude
        self.latitude = latitude
        self.number_of_images = number_of_images

    def __str__(self):
        """A method converting the Request object into a printable string"""
        return f"Request #{self.id}: (longitude: {self.longitude}, latitude: {self.latitude}, number_of_images: {self.number_of_images})"

    def check_logic(self, spacecraft):
        """A method to verify the Request logic"""
        flag = true

        return flag

def create_app():
    app = Flask(__name__)

    return app
