#!/usr/bin/python3
'''
Implements unittests for state.py
'''
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    '''tests edge cases for the State class - instantiation'''

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_id_type(self):
        state = State()
        self.assertEqual(str, type(state.id))

    def test_created_at_type(self):
        state = State()
        self.assertEqual(datetime, type(state.created_at))

    def test_updated_at_type(self):
        state = State()
        self.assertEqual(datetime, type(state.updated_at))

    def test_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_different_created_at(self):
        state1 = State()
        sleep(0.5)
        state2 = State()
        self.assertNotEqual(state1.created_at, state2.created_at)

    def test_different_updated_at(self):
        state1 = State()
        sleep(0.5)
        state2 = State()
        self.assertNotEqual(state1.updated_at, state2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = dt
        statestr = state.__str__()
        self.assertIn("[State] (123456)", statestr)
        self.assertIn("'id': '123456'", statestr)
        self.assertIn("'created_at': " + dt_repr, statestr)
        self.assertIn("'updated_at': " + dt_repr, statestr)

    def test_args_unused(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)


class TestState_save(unittest.TestCase):
    '''tests edge cases for the State class - save method'''

    def test_one_save(self):
        state = State()
        sleep(0.1)
        up = state.updated_at
        state.save()
        self.assertLess(up, state.updated_at)

    def test_two_saves(self):
        state = State()
        sleep(0.1)
        up = state.updated_at
        state.save()
        up2 = state.updated_at
        self.assertLess(up, up2)
        sleep(0.1)
        state.save()
        self.assertLess(up2, state.updated_at)

    def test_save_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)


class TestState_to_dict(unittest.TestCase):
    '''tests edge cases for the State class - to_dict method'''

    def test_to_dict_similarity(self):
        self.assertNotEqual(State().to_dict(), State().__dict__)

    def test_to_dict_type(self):
        self.assertEqual(dict, type(State().to_dict()))

    def test_correct_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_added_values_exist(self):
        state = State()
        state.name = "asma"
        state.my_number = 13
        self.assertIn("name", state.to_dict())
        self.assertIn("my_number", state.to_dict())

    def test_to_dict_datetime_attributes_type(self):
        state = State()
        _dict = state.to_dict()
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = dt
        _dict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(state.to_dict(), _dict)

    def test_to_dict_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)


if __name__ == "__main__":
    unittest.main()
