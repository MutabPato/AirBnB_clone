#!/usr/bin/python3
"""
Parent class
takes care of the initialization, serialization
and deserialization of future instances
"""


import uuid
import datetime
import json
import models


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize our class instances
        id: string - assign with an uuid when an instance is created
        created_at: assign current datetime when instance is created
        updated_at: assign current datetime when instance is created
        and it will be updated every time you change your object
        """
        if kwargs:
            if kwargs.get('id') is None:
                kwargs['id'] = str(uuid.uuid4())
                kwargs['created_at'] = datetime.datetime.now()
                kwargs['updated_at'] = datetime.datetime.now()
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.fromisoformat(value)
                setattr(self, key, value)
            models.storage.new(self)
            models.storage.save()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        prints class name, id and dictionary representation of our class
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with current datetime
        """

        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns dictionary containing all keys/values of __dict__ of instance
        """

        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return (model_dict)
