"""
This file has some test classes related to implementation the class vehicle

Author: Sergio Sanabria <sasanabriac@udistrital.edu.co>
"""
import unittest
from unittest.mock import Mock
from workshop_pro.vehicles_subsystem.vehicle import Vehicle

class TestVehicle(unittest.TestCase):
    "This class contains the tests for the vehicles"

    def setUp(self):
        """Set up the test environment."""
        self.engine_mock = Mock()
        self.vehicle = Vehicle("ABC123", 20000, self.engine_mock, "Modelo", 2022)

    def test_is_in_year(self):
        """Verify that the vehicle is within the range of years""" 
        self.assertTrue(self.vehicle.is_in_year(2020, 2025))
        self.assertFalse(self.vehicle.is_in_year(2023, 2025))

    def test_is_in_speed(self):
        """Simulate the behavior of the engine"""
        self.engine_mock.is_in_speed.return_value = True
        self.assertTrue(self.vehicle.is_in_speed(100, 200))
        self.engine_mock.is_in_speed.return_value = False
        self.assertFalse(self.vehicle.is_in_speed(100, 200))

    def test_is_in_price(self):
        """Verify that the vehicle is within the price range"""
        self.assertTrue(self.vehicle.is_in_price(15000, 25000))
        self.assertFalse(self.vehicle.is_in_price(25000, 30000))

    def test_is_chassis(self):
        """Verify if the vehicle has the same chassis"""
        self.assertTrue(self.vehicle.is_chassis("ABC123"))
        self.assertFalse(self.vehicle.is_chassis("XYZ789"))

if __name__ == "__main__":
    unittest.main()
