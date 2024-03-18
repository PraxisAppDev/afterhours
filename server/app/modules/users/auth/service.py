from datetime import datetime
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.modules.users.auth.util import get_password_hash, verify_password, get_payload
from app.modules.users.service import service as user_service
from app.modules.users.router_models import UpdateUserModel, UserCreateModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/auth/token")

class AuthService():
  async def authenticate_user(self, username: str, plain_password: str):
    user = await user_service.find_user_by_username(username)
    if not user or not verify_password(plain_password, user["hashedPassword"]):
      return None
    else:
      return user
    
  async def log_user_sign_in(self, id) -> bool:
    await user_service.update_user_by_id(id, UpdateUserModel(
      lastLogin=datetime.now()
    ))
    
  async def create_new_user(self, username: str, email: str, fullname: str, password: str) -> str:
    if await user_service.find_user_by_username(username) or await user_service.find_user_by_email(email):
      return None
    else:
      new_user = UserCreateModel(
        username=username,
        email=email,
        fullname=fullname,
        hashedPassword=get_password_hash(password),
        lastLogin=datetime.now()
      )
      new_user_id = await user_service.add_user(new_user)
      return new_user_id

  async def get_id_with_token(self, token: Annotated[str, Depends(oauth2_scheme)]):
    payload = get_payload(token)
    id = payload.get("_id")
    return id

service = AuthService()