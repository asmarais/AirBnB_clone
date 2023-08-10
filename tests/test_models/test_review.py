#!/usr/bin/python3
'''
Implements unittests for review.py
'''
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    '''tests edge cases for the Review class - instantiation'''

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_id_type(self):
        review = Review()
        self.assertEqual(str, type(review.id))

    def test_created_at_type(self):
        review = Review()
        self.assertEqual(datetime, type(review.created_at))

    def test_updated_at_type(self):
        review = Review()
        self.assertEqual(datetime, type(review.updated_at))

    def test_unique_ids(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_different_created_at(self):
        review1 = Review()
        sleep(0.5)
        review2 = Review()
        self.assertNotEqual(review1.created_at, review2.created_at)

    def test_different_updated_at(self):
        review1 = Review()
        sleep(0.5)
        review2 = Review()
        self.assertNotEqual(review1.updated_at, review2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        review = Review()
        review.id = "123456"
        review.created_at = review.updated_at = dt
        reviewstr = review.__str__()
        self.assertIn("[Review] (123456)", reviewstr)
        self.assertIn("'id': '123456'", reviewstr)
        self.assertIn("'created_at': " + dt_repr, reviewstr)
        self.assertIn("'updated_at': " + dt_repr, reviewstr)

    def test_args_unused(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        review = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(review.id, "345")
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        review = Review("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(review.id, "345")
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)


class TestReview_save(unittest.TestCase):
    '''tests edge cases for the Review class - save method'''

    def test_one_save(self):
        review = Review()
        sleep(0.1)
        up = review.updated_at
        review.save()
        self.assertLess(up, review.updated_at)

    def test_two_saves(self):
        review = Review()
        sleep(0.1)
        up = review.updated_at
        review.save()
        up2 = review.updated_at
        self.assertLess(up, up2)
        sleep(0.1)
        review.save()
        self.assertLess(up2, review.updated_at)

    def test_save_with_arg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)


class TestReview_to_dict(unittest.TestCase):
    '''tests edge cases for the Review class - to_dict method'''

    def test_to_dict_similarity(self):
        self.assertNotEqual(Review().to_dict(), Review().__dict__)

    def test_to_dict_type(self):
        self.assertEqual(dict, type(Review().to_dict()))

    def test_correct_keys(self):
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_added_values_exist(self):
        review = Review()
        review.name = "asma"
        review.my_number = 13
        self.assertIn("name", review.to_dict())
        self.assertIn("my_number", review.to_dict())

    def test_to_dict_datetime_attributes_type(self):
        review = Review()
        _dict = review.to_dict()
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        review = Review()
        review.id = "123456"
        review.created_at = review.updated_at = dt
        _dict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(review.to_dict(), _dict)

    def test_to_dict_with_arg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)


if __name__ == "__main__":
    unittest.main()
