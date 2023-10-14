#!/usr/bin/python3
""" Defines unittest models/user.py"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_default_values(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_custom_values(self):
        user = User
        (email="bnb@e.com", password="p123", first_name="Jn", last_name="Bty")
        self.assertEqual(user.email, "hbnb@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Betty")


if __name__ == '__main__':
    unittest.main()
