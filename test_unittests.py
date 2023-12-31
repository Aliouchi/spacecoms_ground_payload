"""Unit Tests"""

from __future__ import annotations

import unittest

# from app import create_app
from logic_checks import date_time_check, distance_check, id_check, total_check
from request_struct import Request
from routing import load_ip
from spacecraft_telem import Spacecraft

# import os
# from flask import Flask, jsonify, request
# from flask_pymongo import PyMongo

#import flask



# @pytest.fixture(scope='module')
# def test_client():
#     """Initializing pytest fixture for appliacation run for flask unit tests"""
#     os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
#     flask_app = create_app()

#     with flask_app.test_client() as testing_client:
#         with flask_app.app_context():
#             yield testing_client


class TestRequestClass(unittest.TestCase):
    """A class consisting of tests for the request object"""
    def test_init_method(self):
        """A test testing the init function of the request object"""
        req = Request("20231020_123012", 43.46, 80.52)

        assert str(req.identifier) == "20231020_123012"
        assert req.longitude == 43.46
        assert req.latitude == 80.52

    def test_str_method(self):
        """A test testing the str function of the request object"""
        req = Request("20231020_123012", 43.46, 80.52)

        assert str(req) == "Request #20231020_123012: (longitude: 43.46, latitude: 80.52)"


class TestSpacecraftTelemClass(unittest.TestCase):
    """A class with tests meant to validate the spacecraft telem object"""
    def test_init_method(self):
        """A test testing the init function of the spacecraft telem object"""
        telem = Spacecraft("20231103_123012", 43.46, 80.52)

        assert str(telem.identifier) == "20231103_123012"
        assert telem.longitude == 43.46
        assert telem.latitude == 80.52

    def test_str_method(self):
        """A test testing the str function of the spacecraft telem object"""
        telem = Spacecraft("20231020_123012", 43.46, 80.52)

        assert str(telem) == "Telem #20231020_123012: longitude: 43.46, latitude: 80.52"


class TestLogicChecks(unittest.TestCase):
    """A class with all the tests required for request logic check"""
    def test_total_check_method(self):
        """A test testing the total_check function of the request object"""
        req = Request("20231020_123012", 43.47, -80.51)
        telem = Spacecraft("20231103_123012", 43.46, -80.50)

        assert total_check(req, telem)

    def test_distance_check_method(self):
        """A test testing the distance_check function of the request object"""
        req = Request("20231020_123012", 43.47, -80.51)
        telem = Spacecraft("20231103_123012", 43.46, -80.50)

        assert distance_check(req, telem)

    def test_id_check_method(self):
        """A test testing the id_check function of the request object"""
        req = Request("20231020_123012", 43.46, 80.52)

        assert id_check(req)

    def test_date_time_check_method(self):
        """A test testing the date_time_check function of the request object"""
        req = Request("20231020_123012", 43.46, 80.52)

        assert date_time_check(req)


    def test_distance_check_within_max_distance(self):
        """A happy path test for the distance_check function"""
        request = Request("20231019_233715", 0.00, 0.00)
        spacecraft = Spacecraft("20231020_123012", 0.00, 0.00)
        self.assertTrue(distance_check(request, spacecraft))

    def test_distance_check_beyond_max_distance(self):
        """A sad path test for the distance_check function"""
        request = Request("20231019_233715", 0.00, 0.00)
        spacecraft = Spacecraft("20231020_123012", 1.01, 1.01)
        self.assertFalse(distance_check(request, spacecraft))

    def test_id_check_valid_format(self):
        """A happy path test for the id_check function"""
        request = Request("20231019_233715", 0.00, 0.00)
        self.assertTrue(id_check(request))

    def test_id_check_invalid_format(self):
        """A sad path test for the id_check function"""
        request = Request("20231019_2337X5", 0.00, 0.00)
        self.assertFalse(id_check(request))

    def test_date_time_check_valid_date_time(self):
        """A happy path test for the date_time_check function"""
        request = Request("20231019_233715", 0.00, 0.00)
        self.assertTrue(date_time_check(request))

    def test_date_time_check_invalid_date_time(self):
        """A sad path test for the date_time_check function"""
        request = Request("20231345_256789", 0.00, 0.00)
        self.assertFalse(date_time_check(request))

    def test_total_check_valid_request(self):
        """A happy path test for the total_check function"""
        request = Request("20231019_233715", 0.00, 0.00)
        spacecraft = Spacecraft("20231020_123012", 0.00, 0.00)
        self.assertTrue(total_check(request, spacecraft))

    def test_total_check_invalid_request(self):
        """A sad path test for the total_check function"""
        request = Request("20231345_256789", 0.01, 0.01)
        spacecraft = Spacecraft("20231020_123012", 0.00, 0.00)
        self.assertFalse(total_check(request, spacecraft))

class TestRouting(unittest.TestCase):
    """A class with all the tests to validate routing methods """
    def test_load_ip_5(self):
        """A test checking if load_ip method loads module 5's ip properly"""
        module_5_ip = load_ip(5, "ip_testing.txt")

        assert module_5_ip == "10.144.111.63"

    def test_load_ip_7(self):
        """A test checking if load_ip method loads module 7's ip properly"""
        module_7_ip = load_ip(7, "ip_testing.txt")

        assert module_7_ip == "10.144.111.120"
