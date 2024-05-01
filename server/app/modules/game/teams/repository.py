from collections import defaultdict
from app.database import database
from app.modules.game.teams.router_models import *
import json
from bson import ObjectId
from datetime import datetime, timezone
from asyncio import Lock

class TeamsRepository:
  def __init__(self):
    self.collection = database.get_collection("hunts")
    self.teams_lock = Lock()

  async def create_team(self, hunt_id: str, team_document: Team):
    query = {
      "$push": {
        "gameState.teams": team_document.model_dump()
      }
    }

    condition = {
        "_id": ObjectId(hunt_id),
        "gameState": {"$exists": True, "$ne": None}
    }
    
    # Update the document with _id "ABCDE" only if gameState is not null
    result = await self.collection.update_one(condition, query)
    
    # If gameState is null or doesn't exist, initialize it with an empty teams array and add the team
    if result.matched_count == 0:
        await self.collection.update_one({"_id": ObjectId(hunt_id)}, {"$set": {"gameState": {"teams": [team_document.model_dump()]}}})

    if result:
      return team_document
    
  async def request_join_team(self, id_hunt: str, team_id: str, id_user: str):
    async with self.teams_lock:
      hunt = await self.collection.find_one({"_id": ObjectId(id_hunt)})
      teams_list = hunt.get("gameState").get("teams")
      team = [team for team in teams_list if team.get("id") == team_id]
      new_teams_list = [team for team in teams_list if team.get("id") != team_id]
      if team[0].get("isLocked"):
        raise Exception("Team is locked")
      if id_user in team[0]["invitations"]:
        raise Exception("User has already requested to join the team")
      if id_user in [player.get("playerId") for player in team[0]["players"]]:
        raise Exception("User is already a member of the team")
      team[0]["invitations"].append(id_user)
      updated_team = team[0]
      new_teams_list.append(updated_team)
      result = await self.collection.update_one({"_id": ObjectId(id_hunt)}, {"$set": {"gameState": {"teams": new_teams_list}}})

    if result:
      return new_teams_list
    
  async def cancel_request_join_team(self, id_hunt: str, team_id: str, id_user: str):
    async with self.teams_lock:
      hunt = await self.collection.find_one({"_id": ObjectId(id_hunt)})
      teams_list = hunt.get("gameState").get("teams")
      team = [team for team in teams_list if team.get("id") == team_id]
      new_teams_list = [team for team in teams_list if team.get("id") != team_id]
      team[0]["players"] = [player for player in team[0]["players"] if player.get("playerId") != id_user]
      updated_team = team[0]
      new_teams_list.append(updated_team)
      result = await self.collection.update_one({"_id": ObjectId(id_hunt)}, {"$set": {"gameState": {"teams": new_teams_list}}})

    if result:
      return new_teams_list
  
  async def respond_join_request(self, id_hunt: str, team_name: str, user_account_id: str, id_joining_user: str, join_request_accepted: bool):
    async with self.teams_lock:
      hunt = await self.collection.find_one({"_id": ObjectId(id_hunt)})
      teams_list = hunt.get("gameState").get("teams")
      team = [team for team in teams_list if team.get("id") == team_name]
      new_teams_list = [team for team in teams_list if team.get("id") != team_name]
      if team[0].get("teamLead") != user_account_id:
        raise Exception(f"Only the team leader can {'accept' if join_request_accepted else 'reject'} join requests")
      
      if join_request_accepted:
        team[0]["players"].append(Player(playerId=id_joining_user, timeJoined=datetime.now()).model_dump())
      team[0]["invitations"] = [invitation for invitation in team[0]["invitations"] if invitation != id_joining_user]
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
        teams = gameState.get("teams")
        return teams if teams is not None else []
      else:
        return []
  
  async def get_team_members(self, id_hunt: str, team_id: str) -> List[Player]:
    hunt = await self.collection.find_one({"_id": ObjectId(id_hunt)})
    hunt_game_state = hunt.get("gameState")
    teams_list = [] if hunt_game_state is None else hunt.get("gameState").get("teams")
    team = [team for team in teams_list if team.get("id") == team_id]
    if team is None or len(team) == 0:
      raise Exception("Team not found")
    return team[0].get("players")
  
  async def get_join_requests(self, id_hunt: str, team_id: str) -> List[str]:
    hunt = await self.collection.find_one({"_id": ObjectId(id_hunt)})
    teams_list = hunt.get("gameState").get("teams")
    team = [team for team in teams_list if team.get("id") == team_id]
    return team[0].get("invitations")
  
  async def remove_member(self, id_hunt: str, team_id: str, member_id: str, authed_user_id: str):
    async with self.teams_lock:
      hunt = await self.collection.find_one({"_id": ObjectId(id_hunt)})
      teams_list = hunt.get("gameState").get("teams")
      team = [team for team in teams_list if team.get("id") == team_id]

      if member_id != authed_user_id and team[0].get("teamLead") != authed_user_id:
        raise Exception("Only the team leader or the member themselves can remove members from a team")

      new_teams_list = [team for team in teams_list if team.get("id") != team_id]
      new_players = [player for player in team[0]["players"] if player.get("playerId") != member_id]
      team_removed = len(new_players) == 0
      if not team_removed:
        team[0]["players"] = new_players
        updated_team = team[0]
        new_teams_list.append(updated_team)
      result = await self.collection.update_one({"_id": ObjectId(id_hunt)}, {"$set": {"gameState": {"teams": new_teams_list}}})

    if result:
      return TeamMemberRemovalSuccessModel(success=True, team_deleted=team_removed)

repository = TeamsRepository()