"""
JWT singleton instance
"""

from flask_jwt_extended import JWTManager

__jwt = {}

def initialize(app):
    """
    Called once in app.py, create an instance that we can get a hold of elsewhere in the app
    """
    __jwt["instance"] = JWTManager(app)

def get_jwt():
    """
    Get the JWT singleton instance
    """
    return __jwt["instance"]
