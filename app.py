"""Running Flask Server"""

from __future__ import annotations

import math
import re
from datetime import datetime

from flask import Flask, render_template, request

# INSERT RADIUS OF THE PLANETARY OBJECT WE ARE RESEARCHING HERE (SET TO PLANET EARTH BY DEFAULT)
PLANET_RADIUS = 6371
# INSERT THE MAX DISTANCE WE WANT THE SPACECRAFT TO GO HERE
MAX_DISTANCE = 10

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

    def __str__(self, spacecraft):
        """A method converting the Request object into a printable string"""
        return f"Request #{self.id}: (longitude: {self.longitude}, latitude: {self.latitude}, number_of_images: {self.number_of_images})"


    def distance_check(self, spacecraft):
        """A method to verify distance from spacecraft to the point we want to take picture"""
        lat1 = self.latitude
        long1 = self.longitude
        lat2 = spacecraft.latitude
        long2 = spacecraft.longitude

        # Calculating Distance using the Haversine Formula
        distance = math.acos(((math.sin(lat1) * math.sin(lat2)) + (math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1))) * PLANET_RADIUS)

        if(distance < MAX_DISTANCE):
            return True
        else:
            return False


    def images_check(self, spacecraft):
        """A method to verify the number of images requested (needs to be between 1 and 99)"""
        if (self.number_of_images >= 1 and self.number_of_images <= 99):
            return True
        else:
            return False

    def id_check(self):
        """A method to verify the format of the ID provided"""
        regex_flag = False

        regex = re.compile(r"\d{8}_\d{6}")
        if re.fullmatch(regex, self.id):
            regex_flag = True
        else:
            regex_flag = False

        datetime_split = self.id.split("_")
        format = "%Y%m%d"

        if(datetime.strptime(datetime_split[0], format) and regex_flag):
            return True
        else:
            return False

    def date_time_check(self):
        """A method to parse the ID property and check the validity of date & time"""
        datecheck = False

        datetime_split = self.id.split("_")

        year = datetime_split[0][0:4]
        month = datetime_split[0][4:6]
        day = datetime_split[0][6:8]

        hour = datetime_split[1][0:2]
        minute = datetime_split[1][2:4]
        second = datetime_split[1][-2:]

        if(year >= 2000 and month >= 1 and month <= 12 and day >= 1 and day <= 31):
            datecheck = True
        else:
            datecheck = False

        if(hour >= 1 and hour <= 24 and minute >= 0 and minute <= 59 and second >= 0 and second <= 59 and datecheck):
            return True
        else:
            return False
    
        def total_check(self, spacecraft):
        """A method to verify the overall request logic (runs all the individual checks)"""
        flag = False

        if(distance_check(spacecraft) == True, image_check(spacecraft) == True, id_check(spacecraft) == True, date_time_check(spacecraft) == True):
            flag = True
            return flag
        else:
            return flag

def create_app():
    app = Flask(__name__)

    return app
