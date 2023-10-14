#!/usr/bin/python3
"""Defines unittest models/state.py"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_set_attributes(self):
        state = State()
        state.name = "Nigeria"
        self.assertEqual(state.name, "Nigeria")

    def test_from_dict(self):
        state_dict = {
            "name": "Nigeria"
        }
        state = State()
        state.from_dict(state_dict)
        self.assertEqual(state.name, "Nigeria")

    def test_to_dict(self):
        state = State()
        state.name = "Nigeria"
        state_dict = state.to_dict()
        self.assertEqual(state_dict["name"], "Nigeria")


if __name__ == '__main__':
    unittest.main()
