"""
User Model
"""

from passlib.hash import pbkdf2_sha256 as sha256
from app import db


class UserModel(db.Model):
    """
    User Model Class
    """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def save_to_db(self):
        """
        Save user details in Database
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        """
        Find user by username
        """
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_id(cls, id):
        """
        Find user by id
        """
        return cls.query.filter_by(id=id).first()

    @staticmethod
    def generate_hash(password):
        """
        Hash password
        """
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash_value):
        """
        Verify password
        """
        return sha256.verify(password, hash_value)
