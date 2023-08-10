#!/usr/bin/python3
'''
Implements Review class
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Defines a Review'''

    place_id = ""
    user_id = ""
    text = ""
