from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.modules.game.teams.service import service
from app.modules.game.teams.router_models import TeamCreatedSuccesfully, TeamCreationErrorModel
from app.modules.game.teams.router_models import TeamRequestModel
from app.modules.game.teams.router_models import TeamsResponseModel
from typing_extensions import Annotated
from fastapi import Depends
from app.modules.users.auth.service import service as auth_service
from app.util import stream_jsonl_response
from app.exceptions import ValidationErrorsModel

router = APIRouter()

@router.post(
  '/create_team/',
  status_code=201,
  response_model=TeamCreatedSuccesfully,
  responses={
    422: {
      "description": "Request could not be validated",
      "model": ValidationErrorsModel
    },
    500: {
      "description": "Error creating team",
      "model": TeamCreationErrorModel
    }
  }
)
async def create_team(request: TeamRequestModel, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  inserted_team_id = await service.create_team(request)
  return TeamCreatedSuccesfully(message="Team created successfully", inserted_team_id=inserted_team_id)

@router.post(
  '/join_team/{team_name}',
  status_code=201,
  response_model=TeamsResponseModel,
  responses={
    422: {
      "description": "Request could not be validated",
      "model": ValidationErrorsModel
    },
    500: {
      "description": "Error joining team",
      "model": TeamsResponseModel
    } 
  }
)
async def join_team(hunt_id: str, team_name: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  teams_list = await service.join_team(hunt_id, team_name, id_user)
  return TeamsResponseModel(
    message="joined team",
    content=teams_list
  )

@router.get(
  '/list_teams',
  status_code=200,
  response_model=TeamsResponseModel,
  responses={
    422: {
      "description": "Request could not be validated",
      "model": ValidationErrorsModel
    },
    500: {
      "description": "Error getting teams",
      "model": TeamsResponseModel
    } 
  }
)
async def get_teams(hunt_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  teams_list = await service.get_teams(hunt_id)
  return TeamsResponseModel(
    message="Get teams successful",
    content=teams_list
  )

@router.get(
  '/listen_list_teams',
  status_code=200,
  response_class=StreamingResponse,
  responses={
    200: {
      'content': {
        'application/x-ndjson': {}
      }
    },
    422: {
      "description": "Request could not be validated",
      "model": ValidationErrorsModel
    },
  }
)
def listen_teams(hunt_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]) -> StreamingResponse:
  return stream_jsonl_response(service.listen_teams(hunt_id))

@router.get(
  '/{team_id}/members',
  status_code=200,
  responses={
    # to be implemented
  }
)
def get_team_members(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  return service.get_team_members(hunt_id, team_id)

@router.get(
  '/{team_id}/listen_new_join_requests',
  status_code=200,
  response_class=StreamingResponse,
  responses={
    200: {
      'content': {
        'application/x-ndjson': {}
      }
    },
    422: {
      "description": "Request could not be validated",
      "model": ValidationErrorsModel
    },
  }
)
async def watch_join_requests(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  #check that user is team captain
  if not await service.is_team_leader(id_user, hunt_id, team_id):
    return
