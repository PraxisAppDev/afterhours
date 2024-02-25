from app.database import database
from app.modules.hunts.router_models import HuntModel
from app.util import handle_object_id
from datetime import datetime

class HuntRepository:
  def __init__(self):
    self.collection = database.get_collection("hunts")

  async def get_all_past_date(date=datetime.now()):
    cursor = self.collection.find({
      "endDate": {
        "$gte": date
      }
    })
    cursor = cursor.listens_to()
    return list(map(lambda document: handle_object_id(document), await cursor.to_list(1000)))

  async def get_all_before_date(date=datetime.now()):
    cursor = self.collection.find({
      "endDate": {
        "$lt": date
      }
    })
    cursor = cursor.listens_to()
    return list(map(lambda document: handle_object_id(document), await cursor.to_list(1000)))

repository = HuntRepository()