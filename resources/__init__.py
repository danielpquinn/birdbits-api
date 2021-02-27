import lib.jwt

from models.user_model import UserModel

jwt = lib.jwt.get_jwt()

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
  username = jwt_data["sub"]
  return UserModel.find_by_username(username)