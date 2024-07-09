#!/usr/bin/env python3
"""
this is encryption and validation module
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
        Generates a salted & hashed password.

        Args:
                password (str): A string containing the plain text
        Returns:
                bytes: A byte string representing the salted
        """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        Validates the provided password

        Args:
                hashed_password (bytes): A byte string
                password (str): A string containing the plain text

        Returns:
                bool: True if the provided password matches the hashed
                password, False otherwise.
        """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
