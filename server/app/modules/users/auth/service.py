from app.modules.users.auth.util import get_password_hash, verify_password
from app.modules.users.service import service as user_service

class AuthService():
  def __init__(self):
    return None
  
  # TODO - ADD SALT LATER
  async def authenticate_user(self, username: str, plain_password: str):
    user = await user_service.find_user_by_email(username)
    if not user or not verify_password(plain_password, user.hashedPassword):
      return None
    else:
      return user

service = AuthService()