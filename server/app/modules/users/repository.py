from app.database import database
from app.modules.users.models import UpdateUserModel, UserModel
from bson import ObjectId

class UserRepository:
  def __init__(self):
    self.collection = database.get_collection("users")
  
  async def get_all(self):
    cursor = self.collection.find()
    return list(map(lambda document: document, await cursor.to_list(1000)))

  async def find_one_by_id(self, id: str):
    return await self.collection.find_one({"_id": ObjectId(id)})
  
  async def find_one_by_email(self, email: str):
    return await self.collection.find_one({"email": email})
  
  async def find_one_by_username(self, username: str):
    return await self.collection.find_one({"username": username})

  async def add_one(self, user: UserModel) -> str:
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

repository = UserRepository()