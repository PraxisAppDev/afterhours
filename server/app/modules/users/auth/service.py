from datetime import datetime
from app.modules.users.auth.util import get_password_hash, verify_password
from app.modules.users.service import service as user_service
from app.modules.users.router_models import UpdateUserModel, UserModel

class AuthService():
  async def authenticate_user(self, email: str, plain_password: str):
    user = await user_service.find_user_by_email(email)
    if not user or not verify_password(plain_password, user["hashedPassword"]):
      return None
    else:
      return user
    
  async def log_user_sign_in(self, id) -> bool:
    await user_service.update_user_by_id(id, UpdateUserModel(
      lastLogin=datetime.now()
    ))
    
  async def create_new_user(self, username: str, email: str, fullname: str, password: str) -> str:
    if await user_service.find_user_by_email(email) or await user_service.find_user_by_username(username):
      return None
    else:
      new_user = UserModel(
        username=username,
        email=email,
        fullname=fullname,
        hashedPassword=get_password_hash(password),
        lastLogin=datetime.now()
      )
      new_user_id = await user_service.add_user(new_user)
      return new_user_id

service = AuthService()