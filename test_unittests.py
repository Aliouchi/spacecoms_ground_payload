"""Unit Tests"""

from __future__ import annotations

import os
import unittest

#import flask
import pytest

from app import create_app
from logic_checks import (date_time_check, distance_check, id_check,
                          images_check, total_check)
from request_struct import Request
from spacecraft_telem import Spacecraft


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
        req = Request("20231020_123012", 43.46, 80.52, 0)

        assert str(req.identifier) == "20231020_123012"
        assert req.longitude == 43.46
        assert req.latitude == 80.52
        assert req.number_of_images == 0

    def test_str_method(self):
        """A test testing the str function of the request object"""
        req = Request("20231020_123012", 43.46, 80.52, 0)

        assert str(req) == "Request #20231020_123012: (longitude: 43.46, latitude: 80.52, number_of_images: 0)"


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
        req = Request("20231020_123012", 43.47, -80.51, 3)
        telem = Spacecraft("20231103_123012", 43.46, -80.50)

        assert total_check(req, telem)

    def test_distance_check_method(self):
        """A test testing the distance_check function of the request object"""
        req = Request("20231020_123012", 43.47, -80.51, 0)
        telem = Spacecraft("20231103_123012", 43.46, -80.50)

        assert distance_check(req, telem)

    def test_images_check_method(self):
        """A test testing the image_check function of the request object"""
        req = Request("20231020_123012", 43.46, 80.52, 12)

        assert images_check(req)

    def test_id_check_method(self):
        """A test testing the id_check function of the request object"""
        req = Request("20231020_123012", 43.46, 80.52, 0)

        assert id_check(req)

    def test_date_time_check_method(self):
        """A test testing the date_time_check function of the request object"""
        req = Request("20231020_123012", 43.46, 80.52, 0)

        assert date_time_check(req)


    def test_distance_check_within_max_distance(self):
        """A happy path test for the distance_check function"""
        request = Request("20231019_233715", 0.00, 0.00, 10)
        spacecraft = Spacecraft("20231020_123012", 0.00, 0.00)
        self.assertTrue(distance_check(request, spacecraft))

    def test_distance_check_beyond_max_distance(self):
        """A sad path test for the distance_check function"""
        request = Request("20231019_233715", 0.00, 0.00, 10)
        spacecraft = Spacecraft("20231020_123012", 1.01, 1.01)
        self.assertFalse(distance_check(request, spacecraft))

    def test_images_check_valid_number(self):
        """A happy path test for the image_check function"""
        request = Request("20231019_233715", 0.00, 0.00, 10)
        self.assertTrue(images_check(request))

    def test_images_check_invalid_number(self):
        """A sad path test for the image_check function"""
        request = Request("20231019_233715", 0.00, 0.00, 100)
        self.assertFalse(images_check(request))

    def test_id_check_valid_format(self):
        """A happy path test for the id_check function"""
        request = Request("20231019_233715", 0.00, 0.00, 10)
        self.assertTrue(id_check(request))

    def test_id_check_invalid_format(self):
        """A sad path test for the id_check function"""
        request = Request("20231019_2337X5", 0.00, 0.00, 10)
        self.assertFalse(id_check(request))

    def test_date_time_check_valid_date_time(self):
        """A happy path test for the date_time_check function"""
        request = Request("20231019_233715", 0.00, 0.00, 10)
        self.assertTrue(date_time_check(request))

    def test_date_time_check_invalid_date_time(self):
        """A sad path test for the date_time_check function"""
        request = Request("20231345_256789", 0.00, 0.00, 10)
        self.assertFalse(date_time_check(request))

    def test_total_check_valid_request(self):
        """A happy path test for the total_check function"""
        request = Request("20231019_233715", 0.00, 0.00, 10)
        spacecraft = Spacecraft("20231020_123012", 0.00, 0.00)
        self.assertTrue(total_check(request, spacecraft))

    def test_total_check_invalid_request(self):
        """A sad path test for the total_check function"""
        request = Request("20231345_256789", 0.01, 0.01, 100)
        spacecraft = Spacecraft("20231020_123012", 0.00, 0.00)
        self.assertFalse(total_check(request, spacecraft))
