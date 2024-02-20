from app.database import database
from app.modules.users.models import UpdateUserModel, UserModel
from app.util import handle_object_id
from bson import ObjectId

class UserRepository:
  def __init__(self):
    self.collection = database.get_collection("users")
  
  async def get_all(self):
    cursor = self.collection.find()
    return list(map(lambda document: handle_object_id(document), await cursor.to_list(1000)))

  async def find_one_by_id(self, id: str):
    document = await self.collection.find_one({"_id": ObjectId(id)})
    if document:
      return handle_object_id(document)
  
  async def find_one_by_email(self, email: str):
    document = await self.collection.find_one({"email": email})
    if document:
      return handle_object_id(document)

  async def add_one(self, user: UserModel):
    document = dict(user)
    document.pop("id")
    result = await self.collection.insert_one(document)
    if result:
      return str(result.inserted_id)
    
  # TODO
  async def update_one(self, id: str, update: UpdateUserModel):
    result = await self.collection.update_one(
      {"_id": ObjectId(id)},
      {"$set": dict(update)}
    )
    return result.n > 0
  
  # TODO - Add HuntId

  async def delete_one(self, id: str):
    result = await self.collection.delete_one({"_id": ObjectId(id)})
    return result.n > 0

repository = UserRepository()