#!/usr/bin/python3
"""
Second class user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
