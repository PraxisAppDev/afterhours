from app.modules.teams.repository import repository

class TeamService:
  def __init__(self):
    self.repository = repository

  async def create_team(self, team):
    return await self.repository.create_team(team)
  
  async def join_team(self, id_hunt, team_name, id_user):
    return await self.repository.join_team(id_hunt, team_name, id_user)

service = TeamService()