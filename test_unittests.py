"""Unit Tests"""

from __future__ import annotations

import os
import unittest

import flask
import pytest

import model
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

        assert true
