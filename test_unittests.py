"""Unit Tests"""

from __future__ import annotations

import os
import unittest

import flask
import pytest

#import model
from app import Request, create_app


@pytest.fixture(scope='module')
def test_client():
    """Initializing pytest fixture for appliacation run for flask unit tests"""
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

class TestRequestClass(unittest.TestCase):
    """A class consisting of tests for the request object"""
    def test_init_method(self):
        """A test testing the init function of the request object"""
        r = Request("20231020_123012", 43.46, 80.52, 0)

        assert str(r.id) == "20231020_123012"
        assert r.longitude == 43.46
        assert r.latitude == 80.52
        assert r.number_of_images == 0

    def test_str_method(self):
        """A test testing the str function of the request object"""
        r = Request("20231020_123012", 43.46, 80.52, 0)

        assert str(r.id) == "Request #20231020_123012: (longitude: 43.46, latitude: 80.52, number_of_images: 0)"

    def test_check_logic_method(self):
        """A test testing the check_logic function of the request object"""
        r = Request("20231020_123012", 43.46, 80.52, 0)

        #TODO: to be implemented

    def test_distance_check_within_max_distance(self):
     request = Request("20231019_233715",0.00,0.00,10)
     spacecraft = Spacecraft(0.00,0.00)
     self.assertTrue(request.distance_check(spacecraft))
     
     
    def test_distance_check_beyond_max_distance(self):
        request = Request("20231019_233715", 0.00, 0.00, 10)
        spacecraft = Spacecraft(0.01, 0.01)
        self.assertFalse(request.distance_check(spacecraft))

    def test_images_check_valid_number(self):
        request = Request("20231019_233715", 0.00, 0.00, 10)
        self.assertTrue(request.images_check())

    def test_images_check_invalid_number(self):
        request = Request("20231019_233715", 0.00, 0.00, 100)
        self.assertFalse(request.images_check())

    def test_id_check_valid_format(self):
        request = Request("20231019_233715", 0.00, 0.00, 10)
        self.assertTrue(request.id_check())

    def test_id_check_invalid_format(self):
        request = Request("20231019_2337X5", 0.00, 0.00, 10)
        self.assertFalse(request.id_check())

    def test_date_time_check_valid_date_time(self):
        request = Request("20231019_233715", 0.00, 0.00, 10)
        self.assertTrue(request.date_time_check())

    def test_date_time_check_invalid_date_time(self):
        request = Request("20231345_256789", 0.00, 0.00, 10)
        self.assertFalse(request.date_time_check())

    def test_total_check_valid_request(self):
        request = Request("20231019_233715", 0.00, 0.00, 10)
        spacecraft = Spacecraft(0.00, 0.00)
        self.assertTrue(request.total_check(spacecraft))

    def test_total_check_invalid_request(self):
        request = Request("20231345_256789", 0.01, 0.01, 100)
        spacecraft = Spacecraft(0.00, 0.00)
        self.assertFalse(request.total_check(spacecraft))

       
