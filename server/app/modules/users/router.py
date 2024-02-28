from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from app.modules.users.service import service as user_service
from app.modules.users.auth.service import service as auth_service
from app.modules.users.auth import router as auth
from app.modules.users.router_models import UpdateUserModel, UserResponseModel, UserResponseTextModel
from app.exceptions import ValidationErrorsModel
from typing_extensions import Annotated

router = APIRouter()

router.include_router(
    auth.router,
    prefix="/auth",
)

# debugging purposes
# @router.get(
#     "/get_all_users",
#     status_code=200,
#     response_model=UserResponseModel
# )
# async def get_all_users():
#   return UserResponseModel(
#     message=UserResponseTextModel.USER_FOUND,
#     content=await user_service.get_users()
#   )

@router.get(
  "/get_user_info",
  status_code=200,
  response_model=UserResponseModel,
  responses={
    404: {
      "description": UserResponseTextModel.USER_NOT_FOUND,
      "model": UserResponseModel
    },
    422: {
      "description": "Request could not be validated",
      "model": ValidationErrorsModel
    }
  }
)
async def find_user_by_id(
  id: Annotated[str, Depends(auth_service.get_id_with_token)]
):
  result = await user_service.find_user_by_id(id)
  if result:
    return UserResponseModel(
      message=UserResponseTextModel.USER_FOUND,
      content=result
    )
  else:
    return JSONResponse(
      status_code=404,
      content=UserResponseModel(
        message=UserResponseTextModel.USER_NOT_FOUND,
        content=""
      ).model_dump()
    )

@router.put(
  "/update_user_info",
  status_code = 200,
  response_model=UserResponseModel,
  responses={
    404: {
      "description": "User not found",
      "model": UserResponseModel
    },
    422: {
      "description": "Request could not be validated",
      "model": ValidationErrorsModel
    }
  }
)
async def update_user_by_id(id: Annotated[str, Depends(auth_service.get_id_with_token)], user: UpdateUserModel):
  result = await user_service.update_user_by_id(id, user)
  if result:
    return UserResponseModel(
      message=UserResponseTextModel.USER_UPDATED,
      content=result
    )
  else:
    return JSONResponse(
      status_code=404,
      content=UserResponseModel(
        message=UserResponseTextModel.USER_NOT_FOUND,
        content=""
      ).model_dump()
    )

@router.delete(
  "/delete_user",
  status_code=200,
  response_model=UserResponseModel,
  responses={
    404: {
      "description": "User not found",
      "model": UserResponseModel
    },
    422: {
      "description": "Request could not be validated",
      "model": ValidationErrorsModel
    }
  },
)
async def delete_user_by_id(id: Annotated[str, Depends(auth_service.get_id_with_token)]):
  result = await user_service.delete_user_by_id(id)
  if result:
    return UserResponseModel(
      message=UserResponseTextModel.USER_DELETED,
      content=result
    )
  else:
    return JSONResponse(
      status_code=404,
      content=UserResponseModel(
        message=UserResponseTextModel.USER_NOT_FOUND,
        content=""
      ).model_dump()
    )
  
@router.get(
  "/get_hunt_history",
  status_code=200,
  response_model=UserResponseModel
)
async def load_list_of_hunts_for_user(
  id: Annotated[str, Depends(auth_service.get_id_with_token)]
):
  result = await user_service.get_hunt_ids_for_user(id)
  # TODO - Use Hunt Service to get hunt model for each hunt id
  return UserResponseModel(
    message=UserResponseTextModel.HUNTS_FOUND,
    content=result
  )
