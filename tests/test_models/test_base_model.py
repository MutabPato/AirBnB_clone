#!/usr/bin/python3
"""
BaseModel test suite
"""

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test all methods and attributes in BaseModel
    """

    def setUp(self):
        """
        Creates instance of BaseModel before each test
        """

        self.base_model = BaseModel()

    def test_is_id_string(self):
        """
        Test if id is a string
        """

        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test if created_at type is datetime
        """

        self.assertIsInstance(self.base_model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if created_at type is datetime
        """

        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        """
        Test if save updates updated_at
        """
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(
                self.base_model.updated_at, original_updated_at)

    def test_to_dict_contains_class_name(self):
        """
        Test if dict contains class_name
        """

        model_dict = self.base_model.to_dict()
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at_and_updated_at(self):
        """
        Test if dict contains created_at and updated_at
        """

        model_dict = self.base_model.to_dict()
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_from_dict_with_no_kwargs_deserialization(self):
        """
        Test if deserialization has correctly been performed
        """
        json_dict = {}
        new_model = BaseModel(**json_dict)
        self.assertIsInstance(new_model.id, str)
        self.assertIsInstance(new_model.created_at, datetime.datetime)
        self.assertIsInstance(new_model.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
