from fastapi import APIRouter
from app.modules.hunts.service import service
from app.modules.hunts.models import HuntModel, HuntResponseModel

router = APIRouter()

@router.get("/load_list_of_hunts")
async def load_list_of_hunts(
  status_code=200,
  response_model=HuntResponseModel
):
  result = await service.get_hunts()
  return HuntResponseModel(
    message="fetched hunts",
    content=result
  )