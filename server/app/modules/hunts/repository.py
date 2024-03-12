from app.database import database
from app.modules.hunts.router_models import ChallengeModel
from app.util import handle_object_id
from datetime import datetime
import json


class HuntRepository:
  def __init__(self):
    self.collection = database.get_collection("hunts")

  async def get_all_past_date(self, date=datetime.now()):
    cursor = self.collection.find({
      "endDate": {
        "$gte": date
      }
    })
    # cursor = cursor.listens_to()
    return list(map(lambda document: handle_object_id(document), await cursor.to_list(1000)))

  async def get_all_before_date(self, date=datetime.now()):
    cursor = self.collection.find({
      "endDate": {
        "$lt": date
      }
    })
    cursor = cursor.listens_to()  # TODO: probably have to remove this line
    return list(map(lambda document: handle_object_id(document), await cursor.to_list(1000)))

  async def create_hunt(self, hunt_document: ChallengeModel):
    result = await self.collection.insert_one(json.loads(hunt_document.json()))
    if result:
      return str(result.inserted_id)


repository = HuntRepository()
