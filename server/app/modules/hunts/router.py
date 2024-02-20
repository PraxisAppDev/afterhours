from fastapi import APIRouter
from app.modules.hunts.service import service
from app.modules.hunts.models import HuntModel, HuntResponseModel

router = APIRouter()

# TODO (Josiah)
@router.get("/")
async def load_list_of_hunts(
  status_code=200,
):
  return "bruh"