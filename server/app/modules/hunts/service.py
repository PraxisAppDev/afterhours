from app.modules.hunts.repository import repository
from datetime import datetime


class HuntService:
  def __init__(self):
    self.repository = repository

  async def get_upcoming(self):
    return await self.repository.get_all_past_date(date=datetime.now())
  
  async def get_past(self):
    return await self.repository.get_all_before_date(date=datetime.now())

  async def create_hunt(self, hunt_challenge):
    return await self.repository.create_hunt(hunt_challenge)


service = HuntService()
