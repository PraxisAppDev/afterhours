from app.modules.hunts.repository import repository
from datetime import datetime

class HuntService:
  def __init__(self):
    self.repository = repository

  async def get_upcoming(self):
  # TODO: just hardcode return a json object with crap data
    return [
      {
        "name": "Recruit Mixer",
        "location": "COORDINATES",
        "date": "March 15"
      },
      {
        "name": "Friday Employee Drinks",
        "location": "COORDINATES",
        "date": "March 16"
      },
      {
        "name": "End of Quarter Party",
        "location": "COORDINATES",
        "date": "March 17"
      }
    ]
    return await self.repository.get_all_past_date(date=datetime.now())
  
  
  async def get_past(self):
    return await self.repository.get_all_before_date(date=datetime.now())

service = HuntService()