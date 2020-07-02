#!/usr/bin/python3
"""Test Module for BaseModel"""


import unittest
from models.base_model import BaseModel
import models
#import pep8
import datetime


class TestHbRequirements(unittest.TestCase):
    """Tests for Holberton Requirements"""

    def tet_style(self):
        """Test for PEP-8 style."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_mod_doc(self):
        """Checks the module documentation"""
        self.assertGreater(len(models.base_model.__doc__), 0)

    def test_cls_doc(self):
        """Checks the class documentation"""
        self.assertGreater(len(BaseModel.__doc__), 0)


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""

    def setUp(self):
        """Set up an object for testing"""
        self.obj = BaseModel()
        self.obj.name = "Betty"
        self.obj.num = 0
        self.obj2 = BaseModel()
        self.obj2.name = "Holberton"
        self.obj2.num = 8
        self.obj3 = BaseModel([1, 2, 3, 4])
        self.obj4 = {
            "name": "nicolas",
            "age": 21
        }
        self.obj5 = self.obj.to_dict()
        self.obj6 = BaseModel(self.obj5)
        self.obj7 = BaseModel(False)

    def test_attr(self):
        """Test the existence of the id attribute"""

        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, "name"))
        self.assertFalse(hasattr(self.obj, "age"))
        self.assertEqual(type(self.obj.id), str)
        self.assertEqual(type(self.obj.created_at), datetime.datetime)
        self.assertEqual(type(self.obj.num), int)

    def test_id(self):
        """Check for the id generator"""

        self.assertNotEqual(self.obj.id, self.obj2.id)

    def test_created_at(self):
        """Check for the created_at attribute's format"""

        now = datetime.datetime.today()
        day = now.today
        self.assertEqual(self.obj.created_at.today, day)

    def test_str_rep(self):
        """Checks for the __str__ method"""

        self.assertEqual(self.obj.__str__(), "[{}] ({}) {}".format(
                         self.obj.__class__.__name__, self.obj.id,
                         self.obj.__dict__))

        
    def test_obj_exist(self):
        """Test if obejcts are created"""

        self.assertIsInstance(self.obj, BaseModel)
        self.assertIsInstance(self.obj2, BaseModel)
        self.assertIsInstance(self.obj3, BaseModel)
        self.assertIsInstance(self.obj6, BaseModel)
        self.assertIsInstance(self.obj7, BaseModel)

    def test_dates_type_dict(self):
        """Tests if dates are casted when they go to dict"""

        self.assertIs(type(self.obj5["created_at"]), str)
        self.assertIs(type(self.obj5["updated_at"]), str)

    def test_class_type(self):
        """Tests class type of '__class__' key in dict"""

        self.assertIs(type(self.obj5["__class__"]), str)

    def test_same_class(self):
        """Tests if two object are part of the same class"""

        self.assertIsNot(self.obj, self.obj6)

    def test_dict_class_attr(self):
        """Tests dict attr with dict key"""

        self.assertNotEqual(self.obj6.__class__, self.obj5["__class__"])
