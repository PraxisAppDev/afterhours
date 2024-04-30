from app.modules.game.teams.repository import repository
from app.util import DatabaseChangeStream, AsyncOnceBox
from app.modules.game.teams.router_models import *
from bson import ObjectId
from typing import List, AsyncIterator

class TeamService:
  def __init__(self):
    self.repository = repository
    self.change_stream = DatabaseChangeStream()

  async def create_team(self, hunt_id, user_id, team_name, is_locked):
    new_team_id = str(ObjectId())
    creator = Player(playerId=user_id, timeJoined=datetime.now())
    team_data = Team(
      id=new_team_id,
      name=team_name,
      teamLead=user_id,
      players=[creator],
      invitations=[],
      isLocked=is_locked
    )
    await self.repository.create_team(hunt_id, team_data)
    self.change_stream.add_change(f'/hunts/{hunt_id}/teams_list', self.__teams_list_change_data(hunt_id))
    # await self.change_stream.add_change(f'/hunts/{hunt_id}/team/{new_team_id}/players_list')
    return team_data
  
  async def request_join_team(self, hunt_id, team_id, id_user):
    await self.repository.request_join_team(hunt_id, team_id, id_user)

    self.change_stream.add_change(f'/hunts/{hunt_id}/teams_list', self.__teams_list_change_data(hunt_id))
    self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/join_requests', self.__join_requests_change_data(hunt_id, team_id))
    return TeamOperationSuccessMessage(message="Join request sent")
  
  async def cancel_request_join_team(self, hunt_id, team_id, id_user):
    await self.repository.cancel_request_join_team(hunt_id, team_id, id_user)
    self.change_stream.add_change(f'/hunts/{hunt_id}/teams_list', self.__teams_list_change_data(hunt_id))
    self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/join_requests', self.__join_requests_change_data(hunt_id, team_id))
    return TeamOperationSuccessMessage(message="Join request cancelled")
  
  async def respond_to_join_request(self, hunt_id, team_id, user_account_id, id_joining_user, join_request_accepted):
    await self.repository.respond_join_request(hunt_id, team_id, user_account_id, id_joining_user, join_request_accepted)
    self.change_stream.add_change(f'/hunts/{hunt_id}/teams_list', self.__teams_list_change_data(hunt_id))
    self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/join_requests', self.__join_requests_change_data(hunt_id, team_id))
    self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/players_list', self.__team_members_change_data(hunt_id, team_id))
    return TeamOperationSuccessMessage(message="Join request accepted")
  
  async def get_teams(self, hunt_id):
    return await self.repository.get_teams(hunt_id)

  async def listen_teams(self, hunt_id):
    yield await self.repository.get_teams(hunt_id)
    async for change in self.change_stream.listen(f'/hunts/{hunt_id}/teams_list'):
      yield await change.get()
  
  async def get_team_members(self, hunt_id, team_id) -> List[Player]:
    return await self.repository.get_team_members(hunt_id, team_id)
  
  async def listen_team_members(self, hunt_id, team_id) -> AsyncIterator[List[Player]]:
    yield await self.repository.get_team_members(hunt_id, team_id)
    async for change in self.change_stream.listen(f'/hunts/{hunt_id}/team/{team_id}/players_list'):
      if change == 'TEAM_DELETED': break
      yield await change.get()
  
  async def get_join_requests(self, hunt_id, team_id) -> List[str]:
    return await self.repository.get_join_requests(hunt_id, team_id)
  
  async def listen_join_requests(self, hunt_id, team_id) -> AsyncIterator[List[str]]:
    yield await self.repository.get_join_requests(hunt_id, team_id)
    async for change in self.change_stream.listen(f'/hunts/{hunt_id}/team/{team_id}/join_requests'):
      if change == 'TEAM_DELETED': break
      yield await change.get()
  
  async def listen_join_request_status(self, hunt_id, team_id, user_id) -> AsyncIterator[str]:
    join_requests = await self.repository.get_join_requests(hunt_id, team_id)
    if user_id in join_requests:
      yield 'pending'
    elif user_id in await self.repository.get_team_members(hunt_id, team_id):
      yield 'accepted'
    else:
      yield 'rejected'
    async for change in self.change_stream.listen(f'/hunts/{hunt_id}/team/{team_id}/join_requests'):
      if change == 'TEAM_DELETED':
        yield 'team_deleted'
        break
      if user_id in await change.get():
        yield 'pending'
      elif user_id in [obj['playerId'] for obj in await self.repository.get_team_members(hunt_id, team_id)]:
        yield 'accepted'
      else:
        yield 'rejected'
  
  async def remove_member(self, hunt_id, team_id, member_id, authed_user_id):
    result = await self.repository.remove_member(hunt_id, team_id, member_id, authed_user_id)
    if result.team_deleted:
      self.change_stream.add_change(f'/hunts/{hunt_id}/teams_list', self.__teams_list_change_data(hunt_id))
      self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/join_requests', 'TEAM_DELETED')
      self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/players_list', 'TEAM_DELETED')
      return TeamOperationSuccessMessage(message="Member removed; Team deleted")
    else:
      self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/players_list', self.__team_members_change_data(hunt_id, team_id))
      return TeamOperationSuccessMessage(message="Member removed")
  
  async def leave_team(self, hunt_id, team_id, user_id):
    result = await self.repository.remove_member(hunt_id, team_id, user_id, user_id)
    if result.team_deleted:
      self.change_stream.add_change(f'/hunts/{hunt_id}/teams_list', self.__teams_list_change_data(hunt_id))
      self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/join_requests', 'TEAM_DELETED')
      self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/players_list', 'TEAM_DELETED')
      return TeamOperationSuccessMessage(message="Left team; Team deleted")
    else:
      self.change_stream.add_change(f'/hunts/{hunt_id}/team/{team_id}/players_list', self.__team_members_change_data(hunt_id, team_id))
      return TeamOperationSuccessMessage(message="Left team")
  
  def __teams_list_change_data(self, hunt_id):
    return AsyncOnceBox(lambda: self.repository.get_teams(hunt_id))
  
  def __team_members_change_data(self, hunt_id, team_id):
    return AsyncOnceBox(lambda: self.repository.get_team_members(hunt_id, team_id))
  
  def __join_requests_change_data(self, hunt_id, team_id):
    return AsyncOnceBox(lambda: self.repository.get_join_requests(hunt_id, team_id))
  



service = TeamService() 