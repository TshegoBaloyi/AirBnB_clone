#!/usr/bin/python3
""" Defines unittest models/amenity.py """

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_default_values(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_custom_values(self):
        amenity = Amenity(name="Jacuzzi")
        self.assertEqual(amenity.name, "Jacuzzi")


if __name__ == '__main__':
    unittest.main()
