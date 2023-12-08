"""A file containing all the logic checks to test the Request"""

from __future__ import annotations

import re
from math import asin, cos, radians, sin, sqrt

# INSERT RADIUS OF THE PLANETARY OBJECT WE ARE RESEARCHING HERE (SET TO PLANET EARTH BY DEFAULT)
PLANET_RADIUS = 6371
# INSERT THE MAX DISTANCE WE WANT THE SPACECRAFT TO GO HERE
MAX_DISTANCE = 10

def total_check(data_request, spacecraft):
    """A method to verify the overall request logic (runs all the individual checks)"""
    flag = False

    if(distance_check(data_request, spacecraft) is True and
        id_check(data_request) is True and date_time_check(data_request) is True):
        flag = True

    return flag

def distance_check(data_request, spacecraft):
    """A method to verify distance from spacecraft to the point we want to take picture"""
    flag = False

    lat1 = data_request.latitude
    long1 = data_request.longitude
    lat2 = spacecraft.latitude
    long2 = spacecraft.longitude

    long_dif = radians(long1 - long2)
    lat_dif = radians(lat1 - lat2)

    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2)

    # Calculating the under sqrt value - let it be x
    a = (pow(sin(lat_dif / 2), 2) + pow(sin(long_dif / 2), 2) * cos(lat1) * cos(lat2))
    # Calculating Distance using the Haversine Formula
    distance = 2 * PLANET_RADIUS * asin(sqrt(a))

    if distance < MAX_DISTANCE:
        flag = True

    return flag



def id_check(data_request):
    """A method to verify the format of the identifier provided"""

    regex = re.compile(r"\d{8}_\d{6}")
    return re.fullmatch(regex, data_request.identifier) is not None


def date_time_check(data_request):
    """A method to parse the identifier property and check the validity of date & time"""
    datecheck = False

    datetime_split = data_request.identifier.split("_")

    year = int(datetime_split[0][0:4])
    month = int(datetime_split[0][4:6])
    day = int(datetime_split[0][6:8])

    hour = int(datetime_split[1][0:2])
    minute = int(datetime_split[1][2:4])
    second = int(datetime_split[1][-2:])

    if(year >= 2000 and month >= 1 and month <= 12 and day >= 1 and day <= 31):
        datecheck = True
    else:
        datecheck = False

    if(hour >= 1 and hour <= 24 and minute >= 0 and minute <= 59 and second >= 0
        and second <= 59 and datecheck):
        return True
    else:
        return False
