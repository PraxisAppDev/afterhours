from typing import List
from app.modules.users.repository import repository
from app.modules.users.router_models import UpdateUserModel, UserCreateModel, UserModel
from app.models import PyObjectId

# TODO
class UserService:
  def __init__(self):
    self.repository = repository

  async def get_users(self):
    return await self.repository.get_all()
  
  async def find_user_by_id(self, id: str) -> UserModel:
    return await self.repository.find_one_by_id(id)

  async def find_user_by_email(self, email: str) -> UserModel:
    return await self.repository.find_one_by_email(email)
  
  async def find_user_by_username(self, username:str) -> UserModel:
    return await self.repository.find_one_by_username(username)

  async def add_user(self, user: UserCreateModel) -> str:
    return await self.repository.add_one(user)

  async def update_user_by_id(self, id: str, update: UpdateUserModel):
    return await self.repository.update_one(id, update)

  async def delete_user_by_id(self, id: str) -> bool:
    return await self.repository.delete_one(id)
  
  # used for testing
  async def delete_user_by_username(self, username: str) -> bool:
    return await self.repository.delete_one_by_username(username)
  
  async def get_hunt_ids_for_user(self, id: str) -> List[PyObjectId]:
    return await self.repository.get_hunt_ids_for_user(id)

service = UserService()