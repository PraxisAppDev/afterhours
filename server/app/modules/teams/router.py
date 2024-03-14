from fastapi import APIRouter
from app.modules.teams.service import service
from app.modules.teams.router_models import TeamCreatedSuccesfully, TeamCreationErrorModel
from app.modules.teams.team_models import Team
from app.modules.users.auth.router_models import Token
from app.modules.users.auth.util import create_access_token

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
async def create_team(request: Team):
  return TeamCreatedSuccesfully(message="Team created successfully", inserted_team_id="RAA")

  