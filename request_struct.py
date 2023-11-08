"""A file for request class structure and logic"""

from __future__ import annotations

# INSERT RADIUS OF THE PLANETARY OBJECT WE ARE RESEARCHING HERE (SET TO PLANET EARTH BY DEFAULT)
PLANET_RADIUS = 6371
# INSERT THE MAX DISTANCE WE WANT THE SPACECRAFT TO GO HERE
MAX_DISTANCE = 10

class Request:
    """Request object - a local definition of the request structure"""
    # def __init__(self):
    #    """A method to initialize the Request class"""
    #    self.identifier = "20231019_233715"
    #    self.longitude = 0.00
    #    self.latitude = 0.00
    #    self.number_of_images = 1

    def __init__(self, identifier, longitude, latitude, number_of_images):
        """A method to initialize the Request class"""
        self.identifier = identifier
        self.longitude = longitude
        self.latitude = latitude
        self.number_of_images = number_of_images

    def __str__(self):
        """A method converting the Request object into a printable string"""
        return f"Request #{self.identifier}: (longitude: {self.longitude}, latitude: {self.latitude}, number_of_images: {self.number_of_images})"
