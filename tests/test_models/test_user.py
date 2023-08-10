#!/usr/bin/python3
'''
Implements unittests for user.py
'''
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    '''tests edge cases for the User class - instantiation'''

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_id_type(self):
        user = User()
        self.assertEqual(str, type(user.id))

    def test_created_at_type(self):
        user = User()
        self.assertEqual(datetime, type(user.created_at))

    def test_updated_at_type(self):
        user = User()
        self.assertEqual(datetime, type(user.updated_at))

    def test_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_at(self):
        user1 = User()
        sleep(0.5)
        user2 = User()
        self.assertNotEqual(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        user1 = User()
        sleep(0.5)
        user2 = User()
        self.assertNotEqual(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        userstr = user.__str__()
        self.assertIn("[User] (123456)", userstr)
        self.assertIn("'id': '123456'", userstr)
        self.assertIn("'created_at': " + dt_repr, userstr)
        self.assertIn("'updated_at': " + dt_repr, userstr)

    def test_args_unused(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)


class TestUser_save(unittest.TestCase):
    '''tests edge cases for the User class - save method'''

    def test_one_save(self):
        user = User()
        sleep(0.1)
        up = user.updated_at
        user.save()
        self.assertLess(up, user.updated_at)

    def test_two_saves(self):
        user = User()
        sleep(0.1)
        up = user.updated_at
        user.save()
        up2 = user.updated_at
        self.assertLess(up, up2)
        sleep(0.1)
        user.save()
        self.assertLess(up2, user.updated_at)

    def test_save_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)


class TestUser_to_dict(unittest.TestCase):
    '''tests edge cases for the User class - to_dict method'''

    def test_to_dict_similarity(self):
        self.assertNotEqual(User().to_dict(), User().__dict__)

    def test_to_dict_type(self):
        self.assertEqual(dict, type(User().to_dict()))

    def test_correct_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_added_values_exist(self):
        user = User()
        user.name = "asma"
        user.my_number = 13
        self.assertIn("name", user.to_dict())
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_type(self):
        user = User()
        _dict = user.to_dict()
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        _dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(user.to_dict(), _dict)

    def test_to_dict_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
