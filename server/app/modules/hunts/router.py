from fastapi import APIRouter
from app.modules.hunts.service import service
from app.modules.hunts.router_models import HuntModel, HuntResponseModel, HuntCreatedSuccessfullyModel, HuntCreationErrorModel
# from app.modules.hunts.hunt_models import ChallengeSchema
from app.modules.hunts.hunt_models import HuntSchema
from app.modules.users.auth.router_models import AuthSuccessTextModel

router = APIRouter()

@router.get(
  "/upcoming",
  status_code=200,
  # response_model=HuntResponseModel
)
async def load_upcoming_hunts():
  result = await service.get_upcoming()
  return result
  response = HuntResponseModel(
    message="fetched hunts",
    content=result
  )
  return response

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

@router.post(
  '/create_hunt',
  status_code=201,
  response_model=HuntCreatedSuccessfullyModel,
  responses={
    500: {
      "description": "Error creating hunt",
      "model": HuntCreationErrorModel
    }
  }
)
async def create_hunt(request: HuntSchema):
  inserted_hunt_id = await service.create_hunt(request)
  return HuntCreatedSuccessfullyModel(message="Hunt created successfully", inserted_hunt_id=inserted_hunt_id)

@router.post(
  "/current_hunts",
  status_code=200,
  response_model=HuntResponseModel
)
async def join_hunt():
  #empty method, needs to be implemnted
  result = await service.get_upcoming()
  return HuntResponseModel(
    content=result
  )

