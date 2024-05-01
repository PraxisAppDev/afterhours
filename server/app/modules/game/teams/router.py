from fastapi import APIRouter
from fastapi.responses import StreamingResponse, PlainTextResponse
from app.modules.game.teams.service import service
from app.modules.game.teams.router_models import *
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
async def create_team(hunt_id: str, user_id: Annotated[str, Depends(auth_service.get_id_with_token)], team: InitialTeamData):
  team = await service.create_team(hunt_id, user_id, team.name, team.is_locked)
  return TeamCreatedSuccesfully(team=team)

# you can't join a team without using the invitation process
# @router.post(
#   '/join_team/{team_name}',
#   status_code=201,
#   response_model=TeamsResponseModel,
#   responses={
#     422: {
#       "description": "Request could not be validated",
#       "model": ValidationErrorsModel
#     },
#     500: {
#       "description": "Error joining team",
#       "model": TeamsResponseModel
#     } 
#   }
# )
# async def join_team(hunt_id: str, team_name: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
#   teams_list = await service.join_team(hunt_id, team_name, id_user)
#   return TeamsResponseModel(
#     message="joined team",
#     content=teams_list
#   )

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
async def get_team_members(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  return await service.get_team_members(hunt_id, team_id)

@router.get(
  '/{team_id}/listen_members',
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
def watch_team_members(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  return stream_jsonl_response(service.listen_team_members(hunt_id, team_id))

@router.get(
  '/{team_id}/join_requests',
  status_code=200,
  responses={
    # to be implemented
  },
  response_model=List[str]
)
async def get_join_requests(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]) -> List[str]:
  return await service.get_join_requests(hunt_id, team_id)

@router.get(
  '/{team_id}/listen_join_requests',
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
async def watch_join_requests(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]) -> StreamingResponse:
  return stream_jsonl_response(service.listen_join_requests(hunt_id, team_id))

@router.post(
  '/{team_id}/request_join',
  status_code=201,
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
async def request_join_team(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  try:
    await service.request_join_team(hunt_id, team_id, id_user)
  except Exception as e:
    if str(e) == "User has already requested to join the team":
      ... # just ignore and give status of request
    else:
      raise e
  return stream_jsonl_response(service.listen_join_request_status(hunt_id, team_id, id_user))

@router.post(
  '/{team_id}/join_requests/currentUser/listenStatus',
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
async def listen_join_request_status(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  return await service.listen_join_request_status(hunt_id, team_id, id_user)

@router.post(
  '/{team_id}/cancel_request_join',
  status_code=200,
  responses={
    # to be implemented
  },
  response_model=TeamOperationSuccessMessage
)
async def cancel_request_join_team(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  return await service.cancel_request_join_team(hunt_id, team_id, id_user)

@router.post(
  '/{team_id}/join_requests/{id_joining_user}/accept',
  status_code=200,
  responses={
    # to be implemented
  },
  response_model=TeamOperationSuccessMessage
)
async def accept_join_request(hunt_id: str, team_id: str, id_joining_user: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  return await service.respond_to_join_request(hunt_id, team_id, id_user, id_joining_user, True)

@router.delete(
  '/{team_id}/join_requests/{id_joining_user}',
  status_code=200,
  responses={
    # to be implemented
  },
  response_model=TeamOperationSuccessMessage
)
async def deny_join_request(hunt_id: str, team_id: str, id_joining_user: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  return await service.respond_to_join_request(hunt_id, team_id, id_user, id_joining_user, False)

# we aren't having teams get deleted, except automatically when all members leave
# @router.delete(
#   '/{team_id}',
#   status_code=200,
#   responses={
#     # to be implemented
#   }
# )
# def remove_team(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
#   return service.remove_team(hunt_id, team_id)

@router.delete(
  '/{team_id}/members/{member_id}',
  status_code=200,
  responses={
    # to be implemented
  }
)
async def remove_member(hunt_id: str, team_id: str, member_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  return await service.remove_member(hunt_id, team_id, member_id, id_user)

@router.post(
  '/{team_id}/leave_team',
  status_code=200,
  responses={
    # to be implemented
  }
)
async def leave_team(hunt_id: str, team_id: str, id_user: Annotated[str, Depends(auth_service.get_id_with_token)]):
  return await service.leave_team(hunt_id, team_id, id_user)