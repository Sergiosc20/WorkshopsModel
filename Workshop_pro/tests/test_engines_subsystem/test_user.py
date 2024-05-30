"""
This file has some test classes related to the user register and autenticate

Author: Sergio Sanabria <sasanabriac@udistrital.edu.co>
"""
import unittest
from unittest.mock import patch
from workshop_pro.core_subsystem.user_authentication import Authentication

class TestAuthentication(unittest.TestCase):
    """This class has different test cases to validate users"""

    def test_authenticate_existing_user_success(self):
        """This mhethod is a unit test for the autentication"""
        with patch("builtins.open", unittest.mock.mock_open(read_data='''[
            {"username": "admin", "password": "admin", "grants": {"add_vehicle": true, "remove_vehicle": true, "search_vehicle": true}},
            {"username": "user", "password": "user", "grants": {"add_vehicle": false, "remove_vehicle": false, "search_vehicle": true}},
            {"username": "Carlos", "password": "CARLOS12312", "grants": {"add_vehicle": false, "remove_vehicle": false, "search_vehicle": true}},
            {"username": "sad", "password": "da", "grants": {"add_vehicle": false, "remove_vehicle": false, "search_vehicle": true}}
        ]''')):
            auth = Authentication("admin", "admin")
            self.assertTrue(auth.authenticate())

    def test_register_new_user_success(self):
        """This mhethod is a unit test for the new user
        of the User class"""
        with patch("builtins.open", unittest.mock.mock_open(read_data='''[
            {"username": "admin", "password": "admin", "grants": {"add_vehicle": true, "remove_vehicle": true, "search_vehicle": true}},
            {"username": "user", "password": "user", "grants": {"add_vehicle": false, "remove_vehicle": false, "search_vehicle": true}},
            {"username": "Carlos", "password": "CARLOS12312", "grants": {"add_vehicle": false, "remove_vehicle": false, "search_vehicle": true}},
            {"username": "sad", "password": "da", "grants": {"add_vehicle": false, "remove_vehicle": false, "search_vehicle": true}}
        ]''')):
            auth = Authentication("test_user", "test_password")
            self.assertTrue(auth.register("new_user", "new_password"))

if __name__ == "__main__":
    unittest.main()
