#!/usr/bin/python3
'''
Implements unittests for place.py
'''
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    '''tests edge cases for the Place class - instantiation'''

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_id_type(self):
        place = Place()
        self.assertEqual(str, type(place.id))

    def test_created_at_type(self):
        place = Place()
        self.assertEqual(datetime, type(place.created_at))

    def test_updated_at_type(self):
        place = Place()
        self.assertEqual(datetime, type(place.updated_at))

    def test_unique_ids(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_different_created_at(self):
        place1 = Place()
        sleep(0.5)
        place2 = Place()
        self.assertNotEqual(place1.created_at, place2.created_at)

    def test_different_updated_at(self):
        place1 = Place()
        sleep(0.5)
        place2 = Place()
        self.assertNotEqual(place1.updated_at, place2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = dt
        placestr = place.__str__()
        self.assertIn("[Place] (123456)", placestr)
        self.assertIn("'id': '123456'", placestr)
        self.assertIn("'created_at': " + dt_repr, placestr)
        self.assertIn("'updated_at': " + dt_repr, placestr)

    def test_args_unused(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        place = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, dt)
        self.assertEqual(place.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        place = Place("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, dt)
        self.assertEqual(place.updated_at, dt)

class TestPlace_save(unittest.TestCase):
    '''tests edge cases for the Place class - save method'''

    def test_one_save(self):
        place = Place()
        sleep(0.1)
        up = place.updated_at
        place.save()
        self.assertLess(up, place.updated_at)

    def test_two_saves(self):
        place = Place()
        sleep(0.1)
        up = place.updated_at
        place.save()
        up2 = place.updated_at
        self.assertLess(up, up2)
        sleep(0.1)
        place.save()
        self.assertLess(up2, place.updated_at)

    def test_save_with_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

class TestPlace_to_dict(unittest.TestCase):
    '''tests edge cases for the Place class - to_dict method'''

    def test_to_dict_similarity(self):
        self.assertNotEqual(Place().to_dict(), Place().__dict__)

    def test_to_dict_type(self):
        self.assertEqual(dict, type(Place().to_dict()))

    def test_correct_keys(self):
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_added_values_exist(self):
        place = Place()
        place.name = "asma"
        place.my_number = 13
        self.assertIn("name", place.to_dict())
        self.assertIn("my_number", place.to_dict())

    def test_to_dict_datetime_attributes_type(self):
        place = Place()
        _dict = place.to_dict()
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = dt
        _dict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(place.to_dict(), _dict)

    def test_to_dict_with_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)

if __name__ == "__main__":
    unittest.main()
