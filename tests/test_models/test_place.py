#!/usr/bin/python3
""" Defines unittest models/place.py """

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_set_attributes(self):
        place = Place()
        place.city_id = "12345"
        place.user_id = "67890"
        place.name = "cozy outdoor trailer"
        place.description = "A charming outdoor trailer in the woods"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.1234
        place.longitude = -122.5432
        place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "67890")
        self.assertEqual(place.name, "Cozy trailer")
        self.assertEqual(place.description, "A trailer in the woods")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.1234)
        self.assertEqual(place.longitude, -122.5432)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])

    def test_to_dict(self):
        place = Place()
        place.city_id = "12345"
        place.user_id = "67890"
        place.name = "Cozy trailer"
        place.description = "A  trailer in the woods"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.1234
        place.longitude = -122.5432
        place.amenity_ids = ["amenity1", "amenity2"]

        place_dict = place.to_dict()
        self.assertEqual(place_dict["city_id"], "12345")
        self.assertEqual(place_dict["user_id"], "67890")
        self.assertEqual(place_dict["name"], "Cozy trailer")
        self.assertEqual(place_dict["description"], "A trailer in the woods")
        self.assertEqual(place_dict["number_rooms"], 2)
        self.assertEqual(place_dict["number_bathrooms"], 1)
        self.assertEqual(place_dict["max_guest"], 4)
        self.assertEqual(place_dict["price_by_night"], 100)
        self.assertEqual(place_dict["latitude"], 37.7749)
        self.assertEqual(place_dict["longitude"], -122.4194)
        self.assertEqual(place_dict["amenity_ids"], ["amenity1", "amenity2"])

    def test_from_dict(self):
        place_dict = {
            "city_id": "12345",
            "user_id": "67890",
            "name": "Cozy traier",
            "description": "A charming outdoor trailer in the woods",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "amenity_ids": ["amenity1", "amenity2"]
        }
        place = Place()
        place.from_dict(place_dict)

        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "67890")
        self.assertEqual(place.name, "Cozy Cabin")
        self.assertEqual(place.description, "A charming cabin in the woods")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])


if __name__ == '__main__':
    unittest.main()
