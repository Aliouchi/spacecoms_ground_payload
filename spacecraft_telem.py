"""A file for spacecraft telemetry class structure and logic"""

from __future__ import annotations


class Spacecraft:
    """Spacecraft object - a local definition of the spacecraft telemetry structure"""

    def __init__(self, identifier, longitude, latitude):
        """A method to initialize the Request class"""
        self.identifier = identifier
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        """A method converting the Request object into a printable string"""
        return f"Telem #{self.identifier}: longitude: {self.longitude}, latitude: {self.latitude}"
