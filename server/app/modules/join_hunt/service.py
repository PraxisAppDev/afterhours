from app.modules.join_hunt import repository
from datetime import datetime

class JoinHuntService:
  def __init__(self):
    self.repository = repository

  async def post_hunt(self):
    return await self.repository.get_all_past_date(date=datetime.now())

service = JoinHuntService()