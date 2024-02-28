from app.database import database
from app.modules.join_hunt.router_models import Join_Hunts_Model
from app.util import handle_object_id
from datetime import datetime

class Join_Hunts_Repository:
  def __init__(self):
    self.collection = database.get_collection("hunts")

  async def get_all_before_date(self, date=datetime.now()):
    cursor = self.collection.find({
      "endDate": {
        "$lt": date
      }
    })
    cursor = cursor.listens_to()
    return list(map(lambda document: handle_object_id(document), await cursor.to_list(1000)))

repository = Join_Hunts_Repository()