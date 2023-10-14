#!/usr/bin/python3
"""" Define unittest models/file_storage.py """

import unittest
import os
from models.base_model import BaseModel
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        self.storage.new(self.model)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertIn("BaseModel." + self.model.id, all_objs)

    def test_new(self):
        all_objs = self.storage.all()
        self.assertNotIn("BaseModel." + self.model.id, all_objs)
        self.storage.new(self.model)
        all_objs = self.storage.all()
        self.assertIn("BaseModel." + self.model.id, all_objs)

    def test_save(self):
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("BaseModel." + self.model.id, all_objs)


if __name__ == '__main__':
    unittest.main()
