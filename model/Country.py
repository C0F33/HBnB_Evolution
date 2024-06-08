#!/usr/bin/python3
import re
import uuid
from datetime import datetime
""" """

class Country:

    def __init__(self, *args, **kwargs):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.update_at = self.creted_at
        self.__name = ""
        self.__code = ""

        if kwargs:
            for key, value in kwargs.items():
                if key == "name" or key == "code":
                    setattr(self, key, value)

    @property
    def name(self):
        """Getter for private prop name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for private prop name"""

        # ensure that the value is not spaces-only and is lettes + spaces only
        val_name = len(value.strip()) > 0 and re.search("^[a-zA-Z ]+$", value)
        if val_name:
            self.__name = value
        else:
            raise ValueError("Invalid country name: {}".format(value))

    @property
    def code(self):
        """Getter for private prop code"""
        return self.__code

    @code.setter
    def code(self, value):
        """Setter for private prop code"""

        # ensure that the value is not spaces and is two uppercase letters
        val_code = len(value.strip()) > 0 and re.search("^[A-Z][A-Z]$", value)
        if val_code:
            self.__code = value
        else:
            raise ValueError("Invalid country code: {}".format(value))
