from app.modules.game.teams.repository import repository
from app.util import DatabaseChangeStream
from app.modules.game.teams.router_models import *
from bson import ObjectId
from typing import List, AsyncIterator

class TeamService:
  def __init__(self):
    self.repository = repository
    self.change_stream = DatabaseChangeStream()

  async def create_team(self, hunt_id, user_id, team_name):
    #print("USER_ID: " + user_id)
    new_team_id = str(ObjectId())
    creator = Player(playerId=user_id, timeJoined=datetime.now())
    team_data = Team(
      id=new_team_id,
      name=team_name,
      teamLead=user_id,
      players=[creator],
      challengeAttempts=[],
      challengeResults=[],
      score=0.0,
      invitations=[]
    )
    await self.repository.create_team(hunt_id, team_data)
    self.change_stream.add_change(f'/hunts/{hunt_id}/teams_list', ("+", team_data))
    # await self.change_stream.add_change(f'/hunts/{hunt_id}/team/{new_team_id}/players_list')
    return team_data
  
  async def request_join_team(self, hunt_id, team_id, id_user):
    await self.repository.request_join_team(hunt_id, team_id, id_user)
    self.change_stream.add_change(f'/hunts/{hunt_id}/teams_list')
    self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/join_requests', ("+", id_user))
    return TeamOperationSuccessMessage(message="Join request sent")
  
  async def cancel_request_join_team(self, hunt_id, team_id, id_user):
    await self.repository.cancel_request_join_team(hunt_id, team_id, id_user)
    self.change_stream.add_change(f'/hunts/{hunt_id}/teams_list')
    self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/join_requests', ("-", id_user))
    return TeamOperationSuccessMessage(message="Join request cancelled")
  
  async def respond_to_join_request(self, hunt_id, team_id, user_account_id, id_joining_user, join_request_accepted):
    await self.repository.respond_join_request(hunt_id, team_id, user_account_id, id_joining_user, join_request_accepted)
    self.change_stream.add_change(f'/hunts/{hunt_id}/teams_list')
    self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/join_requests', ("-", id_joining_user))
    self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/players_list', ("+", id_joining_user))
    return TeamOperationSuccessMessage(message="Join request accepted")
  
  async def get_teams(self, hunt_id):
    return await self.repository.get_teams(hunt_id)

  async def listen_teams(self, hunt_id):
    yield await self.repository.get_teams(hunt_id)
    async for _ in self.change_stream.listen(f'/hunts/{hunt_id}/teams_list'):
      yield await self.repository.get_teams(hunt_id)
  
  async def get_team_members(self, hunt_id, team_id) -> List[Player]:
    return await self.repository.get_team_members(hunt_id, team_id)
  
  async def listen_team_members(self, hunt_id, team_id) -> AsyncIterator[List[Player]]:
    yield await self.repository.get_team_members(hunt_id, team_id)
    async for _ in self.change_stream.listen(f'/hunts/{hunt_id}/team/{team_id}/players_list'):
      yield await self.repository.get_team_members(hunt_id, team_id)
  
  async def get_join_requests(self, hunt_id, team_id) -> List[str]:
    return await self.repository.get_join_requests(hunt_id, team_id)
  
  async def listen_join_requests(self, hunt_id, team_id) -> AsyncIterator[List[str]]:
    yield await self.repository.get_join_requests(hunt_id, team_id)
    async for _ in self.change_stream.listen(f'/hunts/{hunt_id}/team/{team_id}/join_requests'):
      yield await self.repository.get_join_requests(hunt_id, team_id)
  
  async def remove_member(self, hunt_id, team_id, member_id, authed_user_id):
    await self.repository.remove_member(hunt_id, team_id, member_id, authed_user_id)
    self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/players_list', ("-", member_id))
    return TeamOperationSuccessMessage(message="Member removed")
  
  async def leave_team(self, hunt_id, team_id, user_id):
    await self.repository.remove_member(hunt_id, team_id, user_id, user_id)
    self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/players_list', ("-", user_id))
    return TeamOperationSuccessMessage(message="Left team")


service = TeamService() 