from fastapi import APIRouter
from app.modules.teams.service import service
from app.modules.teams.router_models import TeamsResponseModel
from app.modules.teams.team_models import Team
from app.modules.users.auth.router_models import Token
from app.modules.users.auth.util import create_access_token

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
  inserted_hunt_id = await service.create_team(request)
  return TeamsResponseModel(
    message="creating team",
    content=inserted_hunt_id,
    token=Token(
          access_token=create_access_token({"_id": inserted_hunt_id}),
          token_type="bearer"
    )
  )


