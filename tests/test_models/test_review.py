#!/usr/bin/python3
""" Defines unittest for models/review.py """

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_set_attributes(self):
        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "Great place!"
        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "67890")
        self.assertEqual(review.text, "Great place!")

    def test_to_dict(self):
        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "Great place!"
        review_dict = review.to_dict()
        self.assertEqual(review_dict["place_id"], "12345")
        self.assertEqual(review_dict["user_id"], "67890")
        self.assertEqual(review_dict["text"], "Great place!")

    def test_from_dict(self):
        review_dict = {
            "place_id": "12345",
            "user_id": "67890",
            "text": "Great place!"
        }
        review = Review()
        review.from_dict(review_dict)
        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "67890")
        self.assertEqual(review.text, "Great place!")


if __name__ == '__main__':
    unittest.main()
