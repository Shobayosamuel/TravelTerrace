#!/usr/bin/python3
"""Define a class BaseModel that defines common attributes/methods"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This is the base model from which all other models inherits
    """

    def __init__(self, *args, **kwargs):
        """
        This is he instantiation of the class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        This is the string representation
        """
        result = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return result

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        set_dict = self.__dict__.copy()
        set_dict["__class__"] = self.__class__.__name__
        set_dict["created_at"] = self.created_at.isoformat()
        set_dict["updated_at"] = self.updated_at.isoformat()
        return set_dict
