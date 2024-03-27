from app.database import database
from app.modules.hunts.router_models import ChallengeModel
from app.util import handle_object_id
from datetime import datetime
import json


class HuntRepository:
  def __init__(self):
    self.collection = database.get_collection("hunts")

  async def get_all_past_date(self, date=datetime.now()):
    # cursor = self.collection.find({
    #   "endDate": {
    #     "$gte": date
    #   }
    # })
    # # cursor = cursor.listens_to()
    # return list(map(lambda document: handle_object_id(document), await cursor.to_list(1000)))
    current_date = datetime.utcnow()

    # Fetch all documents from the collection
    cursor = self.collection.find({})

    final_response = []

    # Iterate over the cursor
    async for document in cursor:
        # Extract the endDate field from the document
        end_date_str = document.get("endDate")

        # Parse the date string to a datetime object
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d %I:%M %p")

        # Check if the end date is past the current date
        if end_date > current_date:
            print("Hunt is not over yet:", document)
            final_response.append(document)
        else:
            print("Hunt is over:", document)

    return final_response

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
