from app.database import database
from app.modules.hunts.router_models import ChallengeModel
import json


class TeamsRepository:
  def __init__(self):
    self.collection = database.get_collection("hunts")

  async def create_team(self, team_document: ChallengeModel):
    result = await self.collection.insert_one(json.loads(team_document.json()))
    if result:
      return str(result.inserted_id)


repository = TeamsRepository()
