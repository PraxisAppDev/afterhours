from app.modules.hunts.repository import repository
from datetime import datetime

class HuntService:
  def __init__(self):
    self.repository = repository

  async def get_upcoming(self):
    return [
        {
          "title": "Recruit Mixers",
          "location": "The Greene Turtle (In-Person Only)",
          "date": "01/30/024 at 8:30 PM"
        },
        {
          "title": "Friday Employee Drinks",
          "location": "Looney's Pub",
          "date": "02/07/2024 at 7:30 PM"
        },
        {
          "title": "End of Quarter Party",
          "location": "Cornerstone Grill & Loft",
          "date": "02/14/2024 at 7:00 PM"
        }
      ]
    return await self.repository.get_all_past_date(date=datetime.now())
  
  
  async def get_past(self):
    return await self.repository.get_all_before_date(date=datetime.now())

service = HuntService()