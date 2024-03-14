from app.database import database
from app.modules.teams.router_models import TeamRequestModel
import json
from bson import ObjectId


class TeamsRepository:
  def __init__(self):
    self.collection = database.get_collection("hunts")

  async def create_team(self, team_document: TeamRequestModel):
    query = {
      "$push": {
        "gameState.teams": json.loads(team_document.model_dump_json())
      }
    }

    condition = {
        "_id": ObjectId(team_document.hunt_id),
        "gameState": {"$exists": True, "$ne": None}
    }
    
    # Update the document with _id "ABCDE" only if gameState is not null
    result = await self.collection.update_one(condition, query)
    
    # If gameState is null or doesn't exist, initialize it with an empty teams array and add the team
    if result.matched_count == 0:
        await self.collection.update_one({"_id": ObjectId(team_document.hunt_id)}, {"$set": {"gameState": {"teams": []}}})
        await self.collection.update_one({"_id": ObjectId(team_document.hunt_id)}, query)
        
    if result:
      return team_document.name


repository = TeamsRepository()