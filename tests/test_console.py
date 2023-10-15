#!/usr/bin/python3
""" Define unittest console.py """

import os
import sys
import unittest
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("show BaseModel {}".format(obj_id))
                output = f.getvalue().strip()
                self.assertIn(obj_id, output)

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("destroy BaseModel {}".format(obj_id))
                output = f.getvalue().strip()
                self.assertEqual(output, "")

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("all BaseModel")
                output = f.getvalue().strip()
                self.assertIn("BaseModel", output)

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd
                ("update BaseModel {} name 'new name'".format(obj_id))
                output = f.getvalue().strip()
                self.assertEqual(output, "")

    def test_count_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("count BaseModel")
                output = f.getvalue().strip()
                self.assertEqual(output, "1")


if __name__ == '__main__':
    unittest.main()
