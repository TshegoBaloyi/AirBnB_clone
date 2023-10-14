#!/usr/bin/python3
""" Unittest for model/base_model.py"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_dict_returns_dict(self):
        data = self.base_model.to_dict()
        self.assertIsInstance(data, dict)

    def test_to_dict_contains_class_name(self):
        data = self.base_model.to_dict()
        self.assertIn('__class__', data)
        self.assertEqual(data['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at(self):
        data = self.base_model.to_dict()
        self.assertIn('created_at', data)
        self.assertIsInstance(data['created_at'], str)

    def test_to_dict_contains_updated_at(self):
        data = self.base_model.to_dict()
        self.assertIn('updated_at', data)
        self.assertIsInstance(data['updated_at'], str)

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format
        (self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
