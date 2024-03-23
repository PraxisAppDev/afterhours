from fastapi import APIRouter
from app.modules.teams.service import service
from app.modules.teams.router_models import TeamCreatedSuccesfully, TeamCreationErrorModel
from app.modules.teams.router_models import TeamRequestModel
from app.modules.teams.router_models import TeamsResponseModel
from typing_extensions import Annotated
from fastapi import Depends
from app.modules.users.auth.service import service as auth_service

router = APIRouter()

@router.post(
  '/create_team',
  status_code=201,
  response_model=TeamCreatedSuccesfully,
  responses={
    500: {
      "description": "Error creating hunt",
      "model": TeamCreationErrorModel
    } 
  }
)
async def create_team(request: TeamRequestModel):
  inserted_team_id = await service.create_team(request)
  return TeamCreatedSuccesfully(message="Team created successfully", inserted_team_id=inserted_team_id)

@router.post(
  '/join_team',
  status_code=201,
  response_model=TeamsResponseModel,
  responses={
    500: {
      "description": "Error joining team",
      "model": TeamsResponseModel
    } 
  }
)
async def join_team(id_hunt: str, team_name: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  teams_list = await service.join_team(id_hunt, team_name, id_user)
  return TeamsResponseModel(
    message="joined team",
    content=teams_list
  )

@router.post(
  '/get_teams',
  status_code=201,
  response_model=TeamsResponseModel,
  responses={
    500: {
      "description": "Error getting teams",
      "model": TeamsResponseModel
    } 
  }
)
async def get_teams(id_hunt: str):
  teams_list = await service.get_teams(id_hunt)
  return TeamsResponseModel(
    message="Get teams successful",
    content=teams_list
  )
