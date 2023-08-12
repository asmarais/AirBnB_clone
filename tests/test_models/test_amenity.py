#!/usr/bin/python3
'''
Implements unittests for amenity.py
'''
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    '''tests edge cases for the Amenity class - instantiation'''

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_type(self):
        amenity = Amenity()
        self.assertEqual(str, type(amenity.id))

    def test_created_at_type(self):
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.created_at))

    def test_updated_at_type(self):
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.updated_at))

    def test_unique_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_different_created_at(self):
        amenity1 = Amenity()
        sleep(0.5)
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.created_at, amenity2.created_at)

    def test_different_updated_at(self):
        amenity1 = Amenity()
        sleep(0.5)
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.updated_at, amenity2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        amenitystr = amenity.__str__()
        self.assertIn("[Amenity] (123456)", amenitystr)
        self.assertIn("'id': '123456'", amenitystr)
        self.assertIn("'created_at': " + dt_repr, amenitystr)
        self.assertIn("'updated_at': " + dt_repr, amenitystr)

    def test_args_unused(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, dt)
        self.assertEqual(amenity.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity = Amenity("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, dt)
        self.assertEqual(amenity.updated_at, dt)


class TestAmenity_save(unittest.TestCase):
    '''tests edge cases for the Amenity class - save method'''

    def test_one_save(self):
        amenity = Amenity()
        sleep(0.1)
        up = amenity.updated_at
        amenity.save()
        self.assertLess(up, amenity.updated_at)

    def test_two_saves(self):
        amenity = Amenity()
        sleep(0.1)
        up = amenity.updated_at
        amenity.save()
        up2 = amenity.updated_at
        self.assertLess(up, up2)
        sleep(0.1)
        amenity.save()
        self.assertLess(up2, amenity.updated_at)

    def test_save_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)


class TestAmenity_to_dict(unittest.TestCase):
    '''tests edge cases for the Amenity class - to_dict method'''

    def test_to_dict_similarity(self):
        self.assertNotEqual(Amenity().to_dict(), Amenity().__dict__)

    def test_to_dict_type(self):
        self.assertEqual(dict, type(Amenity().to_dict()))

    def test_correct_keys(self):
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())

    def test_added_values_exist(self):
        amenity = Amenity()
        amenity.name = "asma"
        amenity.my_number = 13
        self.assertIn("name", amenity.to_dict())
        self.assertIn("my_number", amenity.to_dict())

    def test_to_dict_datetime_attributes_type(self):
        amenity = Amenity()
        _dict = amenity.to_dict()
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        _dict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(amenity.to_dict(), _dict)

    def test_to_dict_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
