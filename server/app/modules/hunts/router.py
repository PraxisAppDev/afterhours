from fastapi import APIRouter
from app.modules.hunts.service import service
from app.modules.hunts.router_models import HuntModel, HuntResponseModel

router = APIRouter()

@router.get(
  "/upcoming",
  status_code=200,
  # response_model=HuntResponseModel
)
async def load_upcoming_hunts():
  return [
      {
        "title": "Recruit Mixer",
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
  result = await service.get_upcoming()
  return HuntResponseModel(
    message="fetched hunts",
    content=result
  )

@router.get(
  "/history",
  status_code=200,
  response_model=HuntResponseModel
)
async def load_past_hunts():
  result = await service.get_past()
  return HuntResponseModel(
    message="fetched hunts",
    content=result
  )