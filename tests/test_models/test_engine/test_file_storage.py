#!/usr/bin/python3
"""[File Storage Tests Module]"""

import unittest
import pep8
import os
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestHbRequirements(unittest.TestCase):
    """Tests for Holberton Requirements"""

    def test_style(self):
        """Test for PEP-8 style."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_mod_doc(self):
        """Checks the module documentation"""

        self.assertGreater(len(models.engine.file_storage.__doc__), 0)

    def test_cls_doc(self):
        """Checks the class documentation"""

        self.assertGreater(len(FileStorage.__doc__), 0)


class TestFileStorage(unittest.TestCase):
    """Test for FileStorage class"""

    def setUp(self):
        """Default configurations for tests"""

        self.obj = BaseModel()
        self.obj2 = BaseModel()
        self.storage = FileStorage()
        self.storage.new(self.obj)
        self.key = "BaseModel.{}".format(self.obj.id)
        self.dic = self.storage.all()
        self.key2 = "BaseModel.{}".format(self.obj2.id)
        self.dic2 = self.storage.all()

    def test_new_all(self):
        """Test for new method"""

        self.assertIn(self.key, self.dic)
        self.assertIn(self.key2, self.dic2)
        self.assertEqual(self.dic[self.key], self.obj)
        self.assertEqual(self.dic2[self.key2], self.obj2)

    def test_attr_type(self):
        """Test attr types
        """
        self.assertTrue(type(self.dic), dict)

    def test_dict_obj_value(self):
        """test a value of the object stored in dict
        """
        self.assertIn(self.obj, self.dic.values())

    def test_dict_size(self):
        """test dict size
        """
        self.assertEqual(len(self.dic), len(self.storage.all()))
