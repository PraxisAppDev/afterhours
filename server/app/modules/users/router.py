from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import JSONResponse
from app.modules.users.service import service
from app.modules.users.auth import router as auth
from app.modules.users.router_models import UpdateUserModel, UserModel, UserResponseModel, UserResponseTextModel
from app.exceptions import ValidationErrorsModel
from typing_extensions import Annotated

router = APIRouter()

router.include_router(
    auth.router,
    prefix="/auth",
)

@router.get(
  "/{id}",
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
async def find_user_by_id(id: Annotated[str, Path(pattern="^[0-9a-fA-F]{24}$")]):
  result = await service.find_user_by_id(id)
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
  "/{id}",
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
async def update_user_by_id(id: Annotated[str, Path(pattern="^[0-9a-fA-F]{24}$")], user: UpdateUserModel):
  result = await service.update_user_by_id(id, user)
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
  "/{id}",
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
async def delete_user_by_id(id: Annotated[str, Path(pattern="^[0-9a-fA-F]{24}$")]):
  result = await service.delete_user_by_id(id)
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