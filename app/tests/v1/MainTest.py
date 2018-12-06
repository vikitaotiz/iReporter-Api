import unittest
from app import create_app
from flask import current_app

class MainTest(unittest.TestCase):
    def setUp(self):
        app_client = create_app("testing")
        self.app = app_client.test_client()

        self.user_details = {
            "firstname" : "vikita",
            "lastname" : "otiz",
            "username" : "vikitaotiz",
            "password" : "12345"
        }

        self.app_context = app_client.app_context()
        self.app_context.push()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def tearDown(self):
        self.app_context.pop()
