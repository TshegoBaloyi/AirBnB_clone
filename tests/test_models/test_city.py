#!/usr/bin/python3
""" Defines unittest models/city.py"""

import unittest
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    def test_default_values(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_custom_values(self):
        state = State()
        city = City(state_id=state.id, name="Pretoria")
        self.assertEqual(city.state_id, state.id)
        self.assertEqual(city.name, "Pretoria")


if __name__ == '__main__':
    unittest.main()
