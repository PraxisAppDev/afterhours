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
    
  async def join_team(self, id_hunt: str, team_name: str, id_user: str):
    hunt = await self.collection.find_one({"_id": ObjectId(id_hunt)})
    teams_list = hunt.get("gameState").get("teams")
    team = [team for team in teams_list if team.get("name") == team_name]
    new_teams_list = [team for team in teams_list if team.get("name") != team_name]
    team[0]["players"].append(id_user)
    updated_team = team[0]
    new_teams_list.append(updated_team)
    result = await self.collection.update_one({"_id": ObjectId(id_hunt)}, {"$set": {"gameState": {"teams": new_teams_list}}})

    if result:
      return new_teams_list
    
  async def get_teams(self, id_hunt: str):
    hunt = await self.collection.find_one({"_id": ObjectId(id_hunt)})

    if hunt:
      gameState = hunt.get("gameState")
      if gameState:
        return gameState.get("teams")
      else:
        return []

repository = TeamsRepository()