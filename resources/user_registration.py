"""
User registration API
"""

from models.user_model import UserModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                current_user, jwt_required)

register_parser = reqparse.RequestParser()
register_parser.add_argument(
    "email", help="email cannot be blank", required=True)
register_parser.add_argument(
    "username", help="username cannot be blank", required=True)
register_parser.add_argument(
    "full_name", help="full_name cannot be blank", required=True)
register_parser.add_argument(
    "password", help="password cannot be blank", required=True)


class UserRegistration(Resource):
    """
    User registration API
    """

    def post(self):
        """
        Create a new user after verifying that all details are provided
        """
        data = register_parser.parse_args()
        username = data["username"]

        if UserModel.find_by_username(username):
            return {"message": f"User {username} already exists"}

        new_user = UserModel(
            username=username,
            email=data["email"],
            full_name=data["full_name"],
            password=UserModel.generate_hash(data["password"])
        )

        try:
            new_user.save_to_db()

            access_token = create_access_token(
                identity=username, expires_delta=False)

            return {
                "message": f"User {username} was created",
                "access_token": access_token
            }

        except:
            return {"message": "Something went wrong"}, 500
