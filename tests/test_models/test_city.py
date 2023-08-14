#!/usr/bin/python3
'''
Implements unittests for city.py
'''
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    '''tests edge cases for the City class - instantiation'''

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_id_type(self):
        city = City()
        self.assertEqual(str, type(city.id))

    def test_created_at_type(self):
        city = City()
        self.assertEqual(datetime, type(city.created_at))

    def test_updated_at_type(self):
        city = City()
        self.assertEqual(datetime, type(city.updated_at))

    def test_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_different_created_at(self):
        city1 = City()
        sleep(0.5)
        city2 = City()
        self.assertNotEqual(city1.created_at, city2.created_at)

    def test_different_updated_at(self):
        city1 = City()
        sleep(0.5)
        city2 = City()
        self.assertNotEqual(city1.updated_at, city2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        citystr = city.__str__()
        self.assertIn("[City] (123456)", citystr)
        self.assertIn("'id': '123456'", citystr)
        self.assertIn("'created_at': " + dt_repr, citystr)
        self.assertIn("'updated_at': " + dt_repr, citystr)

    def test_args_unused(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city = City("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)


class TestCity_save(unittest.TestCase):
    '''tests edge cases for the City class - save method'''

    def test_one_save(self):
        city = City()
        sleep(0.1)
        up = city.updated_at
        city.save()
        self.assertLess(up, city.updated_at)

    def test_two_saves(self):
        city = City()
        sleep(0.1)
        up = city.updated_at
        city.save()
        up2 = city.updated_at
        self.assertLess(up, up2)
        sleep(0.1)
        city.save()
        self.assertLess(up2, city.updated_at)

    def test_save_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)


class TestCity_to_dict(unittest.TestCase):
    '''tests edge cases for the City class - to_dict method'''

    def test_to_dict_similarity(self):
        self.assertNotEqual(City().to_dict(), City().__dict__)

    def test_to_dict_type(self):
        self.assertEqual(dict, type(City().to_dict()))

    def test_correct_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_added_values_exist(self):
        city = City()
        city.name = "asma"
        city.my_number = 13
        self.assertIn("name", city.to_dict())
        self.assertIn("my_number", city.to_dict())

    def test_to_dict_datetime_attributes_type(self):
        city = City()
        _dict = city.to_dict()
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        _dict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(city.to_dict(), _dict)

    def test_to_dict_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
