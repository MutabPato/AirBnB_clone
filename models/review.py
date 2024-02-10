#!/usr/bin/python3
"""
Seventh class Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
