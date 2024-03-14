from ast import List
from app.database import database
from app.modules.teams.team_models import Team
from app.modules.hunts.router_models import HuntModel
import json


class TeamsRepository:
  def __init__(self):
    self.collection = database.get_collection("hunts")

  async def create_team(self, team_document: Team):
    result = await self.collection.gameState.teams.insert_one(json.loads(team_document.json()))
    if result:
      return str(result.inserted_id)


repository = TeamsRepository()