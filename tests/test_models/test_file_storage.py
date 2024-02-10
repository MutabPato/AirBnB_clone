#!/usr/bin/python3
"""
FileStorage Test Suite
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test instances in FileStorage
    """

    def setUp(self):
        """
        Generate a new instance of FileStorage
        """
        self.storage = FileStorage()

    def test_all(self):
        """
        Test that all() returns a dictionary
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """
        Test that new() adds an object to __objects
        """
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        """
        Test saving and reloading
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn("{}.{}".format(
            obj.__class__.__name__, obj.id), new_storage.all())

    def tearDown(self):
        """
        Sets to None
        """
        self.storage = None


if __name__ == '__main__':
    unittest.main()
