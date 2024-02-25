from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.modules.users.auth.service import service
from app.modules.users.auth.router_models import AuthSuccessModel, AuthSuccessTextModel, AuthErrorModel, AuthErrorTextModel, LoginModel, SignUpModel
from app.modules.users.auth.util import create_access_token
from app.exceptions import ValidationErrorsModel

router = APIRouter()

@router.post(
    "/login",
    status_code=201,
    response_model=AuthSuccessModel,
    responses={
      401: {
        "description": "Incorrect credentials",
        "model": AuthErrorModel
      },
      422: {
        "description": "Request could not be validated",
        "model": ValidationErrorsModel
      }
    }
)
async def login(request: LoginModel):
  user = await service.authenticate_user(request.email, request.password)
  if user:
    await service.log_user_sign_in(user["_id"])
    return AuthSuccessModel(
      message=AuthSuccessTextModel.LOGIN_SUCCESSFUL,
      token=create_access_token({"_id": str(user["_id"])})
    )
  else:
    return JSONResponse(
      status_code=401,
      content=AuthErrorModel(
        message=AuthErrorTextModel.INCORRECT_CREDENTIALS
      ).model_dump()
    )

@router.post(
  "/signup",
  status_code=201,
  response_model=AuthSuccessModel,
  responses={
    422: {
      "description": "Request could not be validated",
      "model": ValidationErrorsModel
    },
    500: {
      "description": "Error creating user",
      "model": AuthErrorModel
    }
  }
)
async def signup(request: SignUpModel):
  new_user_id = await service.create_new_user(request.username, request.email, request.fullname, request.password)
  if new_user_id:
    return AuthSuccessModel(
      message=AuthSuccessTextModel.SIGNUP_SUCCESSFUL,
      token=create_access_token({"_id": new_user_id})
    )
  else:
    raise JSONResponse(
      status_code=500,
      content=AuthErrorModel(
        message=AuthErrorTextModel.INTERNAL_SERVER_ERROR
      ).model_dump()
    )