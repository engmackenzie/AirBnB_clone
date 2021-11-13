#!/usr/bin/python3
"""
Tests for the BaseModel
"""


import unittest
from .models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Contains the actual tests"""

    def setUp(self):
        '''Set up the base by creating an instance of the BaseModel'''
        self.base_model = BaseModel()
        self.base_model1 = BaseModel()

    def test_instances(self):
        """Tests if the instances are created"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model1, BaseModel)

    def test_uuid(self):
        """Testing the uuid
        1. if an instance is created
        2. if instance has an id attribute
        3. if id created in each instance is unique
        """
        self.assertTrue(hasattr(self.base_model, id))
        self.assertTrue(hasattr(self.base_model1, id))
        self.assertNotEqual(self.base_model.id, self.base_model1.id)

    def test_datetime(self):
        """Test the created_at and update_at attributes:
        0. both should be dates
        1. To be equal when instance is created
        2. Should not be equal when save() method is called
        3. test if instances have both attributes
        4. compare to see if both attributes are equal(shouldn't)
        5. create a new instance and check if datetime is
            almost equal to now
        """
    
    def test_str():
        """Tests the __str__ method
        The expected output should be in the format:
        [<class name>] (<self.id>) <self.__dict__>
        """

    def test_todict(self):
        """Tests the to_dict() method:
        1. By using self.__dict__: return only instance attributes
        2. a __class__ key should be added to the dictionary
        3. the datetime(created_at and updated_at should be strings
            format -> %Y-%m-%dT%H:%M:%S.%f
        """
    def tearDown(self):
        """Disposes the instances of the class created"""
        self.base_model.dispose()
        self.base_model1.dispose()