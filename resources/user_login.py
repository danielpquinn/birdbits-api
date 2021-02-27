"""
User login API
"""

from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse
from models.user_model import UserModel

login_parser = reqparse.RequestParser()
login_parser.add_argument(
    "username", help="username cannot be blank", required=True)
login_parser.add_argument(
    "password", help="password cannot be blank", required=True)

class UserLogin(Resource):
    """
    User login resource
    """
    def post(self):
        """
        Verify username and pass, return a JWT
        """
        data = login_parser.parse_args()
        username = data["username"]
        password = data["password"]
        existing_user = UserModel.find_by_username(username)

        if not existing_user:
            return {"message": f"User {username} does not exist"}

        if UserModel.verify_hash(password, existing_user.password):
            access_token = create_access_token(
                identity=username, expires_delta=False)
            return {
                "message": f"Logged in as {username}",
                "access_token": access_token
            }

        else:
            return {"message": "Wrong username or password"}
