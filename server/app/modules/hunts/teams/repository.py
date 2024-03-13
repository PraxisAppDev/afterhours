from app.database import database
from app.modules.hunts.router_models import ChallengeModel
import json

from server.app.util import handle_object_id


class TeamsRepository:
  def __init__(self):
    self.collection = database.get_collection("hunts")

  async def create_team(self, team_document: ChallengeModel):
    result = await self.collection.insert_one(json.loads(team_document.json()))
    if result:
      return str(result.inserted_id)

  async def get_all_teams(self):
    cursor = self.collection.find({})
    # cursor = cursor.listens_to()
    return list(map(lambda document: handle_object_id(document), await cursor.to_list(1000)))




repository = TeamsRepository()