#!/usr/bin/python3
'''
Implements unittests for base_model.py
'''
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    '''tests edge cases for the BaseModel class - instantiation'''

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_type(self):
        bm = BaseModel()
        self.assertEqual(str, type(bm.id))

    def test_created_at_type(self):
        bm = BaseModel()
        self.assertEqual(datetime, type(bm.created_at))

    def test_updated_at_type(self):
        bm = BaseModel()
        self.assertEqual(datetime, type(bm.updated_at))

    def test_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.5)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.5)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    '''tests edge cases for the BaseModel class - save method'''

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.1)
        up = bm.updated_at
        bm.save()
        self.assertLess(up, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.1)
        up = bm.updated_at
        bm.save()
        up2 = bm.updated_at
        self.assertLess(up, up2)
        sleep(0.1)
        bm.save()
        self.assertLess(up2, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)


class TestBaseModel_to_dict(unittest.TestCase):
    '''tests edge cases for the BaseModel class - to_dict method'''

    def test_to_dict_similarity(self):
        self.assertNotEqual(BaseModel().to_dict(), BaseModel().__dict__)

    def test_to_dict_type(self):
        self.assertEqual(dict, type(BaseModel().to_dict()))

    def test_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_added_values_exist(self):
        bm = BaseModel()
        bm.name = "asma"
        bm.my_number = 13
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_type(self):
        bm = BaseModel()
        _dict = bm.to_dict()
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        _dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), _dict)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
