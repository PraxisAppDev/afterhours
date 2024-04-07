from app.modules.game.teams.repository import repository
from app.util import DatabaseChangeStream


class TeamService:
  def __init__(self):
    self.repository = repository
    self.change_stream = DatabaseChangeStream()

  async def create_team(self, team):
    await self.change_stream.add_change({
        "hunt_id": team.hunt_id,
        "team_name": team.name,
    })
    return await self.repository.create_team(team)
  
  async def join_team(self, id_hunt, team_name, id_user):
    await self.change_stream.add_change({
      "hunt_id": id_hunt,
      "team_name": team_name,
    })
    return await self.repository.join_team(id_hunt, team_name, id_user)
  
  async def get_teams(self, id_hunt):
    return await self.repository.get_teams(id_hunt)

  async def listen_teams(self, id_hunt):
    yield await self.repository.get_teams(id_hunt)
    async for team_update in self.change_stream:
      # print("team_update", team_update)
      if team_update["hunt_id"] == id_hunt:
        yield await self.repository.get_teams(id_hunt)


service = TeamService()