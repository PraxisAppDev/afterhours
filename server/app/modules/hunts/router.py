from fastapi import APIRouter
from app.modules.hunts.service import service
from app.modules.hunts.router_models import HuntModel, HuntResponseModel

router = APIRouter()

@router.get(
  "/upcoming",
  status_code=200,
  response_model=HuntResponseModel
)
async def load_upcoming_hunts():
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