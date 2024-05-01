from app.database import database
from app.modules.users.router_models import UpdateUserModel, UserCreateModel, UserModel
from bson import ObjectId

class UserRepository:
  def __init__(self):
    self.collection = database.get_collection("users")
  
  # this method is only for debugging purposes, as listing all users is not a good idea
  async def get_all(self):
    cursor = self.collection.find()
    return list(map(lambda document: document, await cursor.to_list(1000)))
  
  async def find_one_by_id(self, id: str):
    user = await self.collection.find_one({"_id": ObjectId(id)})
    if user is not None: del user["hashedPassword"]
    return user
  
  # this method is for authorization purposes
  async def find_one_by_email(self, email: str):
    return await self.collection.find_one({"email": email})
  
  async def find_one_by_username(self, username: str):
    return await self.collection.find_one({"username": username})

  async def add_one(self, user: UserCreateModel) -> str:
    document = dict(user)
    document.pop("id")
    result = await self.collection.insert_one(document)
    if result:
      return str(result.inserted_id)
    
  # TODO
  async def update_one(self, id: str, update: UpdateUserModel):
    update = {
      k: v for k,v in dict(update).items() if v
    }
    result = await self.collection.update_one(
      {"_id": ObjectId(id)},
      {"$set": update}
    )
    return result.modified_count > 0
  
  # TODO - Add HuntId

  async def delete_one(self, id: str):
    result = await self.collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
  
  async def delete_one_by_username(self, username: str):
    result = await self.collection.delete_one({"username": username})
    return result.deleted_count > 0

  async def get_hunt_ids_for_user(self, id: str):
    cursor = self.collection.find({"_id": ObjectId(id)})
    if cursor:
      return [[str(id) for id in document['huntHistory']] for document in await cursor.to_list(1000)]

repository = UserRepository()