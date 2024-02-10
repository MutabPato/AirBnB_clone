#!/usr/bin/python3
"""
Test suite
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """
    Unittests for the class User
    """

    def setUp(self):
        """
        Set up the test
        """
        self.storage = FileStorage()
        self.storage.reload()
        self.user = User()

    def test_default_attributes(self):
        """
        Test default attributes
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_setting_sttributes(self):
        """
        Sets attributes and test them
        """
        self.user.email = "airbnb@mail.com"
        self.user.password = "root"
        self.user.first_name = "Betty"
        self.user.last_name = "Bar"

        self.assertEqual(self.user.email, "airbnb@mail.com")
        self.assertEqual(self.user.password, "root")
        self.assertEqual(self.user.first_name, "Betty")
        self.assertEqual(self.user.last_name, "Bar")

    def tes_save_method(self):
        """
        Test if the user instance has been saved
        """
        self.user.save()
        user_key = "User.{}".format(self.user.id)
        self.assertIn(key, self.storage.all())

    def test_to_dict_method(self):
        """
        Test if user instance attribute are in it dictionary representation
        """
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last-name)

    def tearDoen(self):
        """
        clean up after the test
        """
        del self.user
        del self.storage


if __name__ == "__main__":
    unittest.main()
