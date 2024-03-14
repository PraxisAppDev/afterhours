from fastapi import APIRouter
from app.modules.teams.service import service
from app.modules.teams.router_models import TeamCreatedSuccesfully, TeamCreationErrorModel
from app.modules.teams.router_models import TeamRequestModel

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

  