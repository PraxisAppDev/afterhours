from fastapi import APIRouter
from app.modules.teams.service import service
from app.modules.teams.router_models import TeamsResponseModel
from app.modules.teams.team_models import Team

router = APIRouter()

@router.post(
  '/create_team',
  status_code=201,
  response_model=TeamsResponseModel,
  responses={
    500: {
      "description": "Error creating hunt",
      "model": TeamsResponseModel
    }
  }
)
async def create_team(request: Team):
  print(request)
  inserted_hunt_id = await service.create_team(request)
  return TeamsResponseModel(
    message="creating team",
    content=inserted_hunt_id
  )


