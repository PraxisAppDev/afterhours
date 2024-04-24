from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.modules.users.auth.service import service
from app.modules.users.auth.router_models import AuthSuccessModel, AuthSuccessTextModel, AuthErrorModel, AuthErrorTextModel, LoginModel, SignUpModel, Token
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
  user = await service.authenticate_user(request.username, request.password)
  if user:
    await service.log_user_sign_in(user["_id"])
    access_token, exp = create_access_token({"_id": str(user["_id"])})
    return AuthSuccessModel(
      message=AuthSuccessTextModel.LOGIN_SUCCESSFUL,
      user_id=str(user["_id"]),
      token=Token(
        access_token=access_token,
        exp=exp,
        token_type="bearer"
      ),
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
  try:
    if new_user_id:
      access_token, exp = create_access_token({"_id": new_user_id})
      return AuthSuccessModel(
        message=AuthSuccessTextModel.SIGNUP_SUCCESSFUL,
        token=Token(
          access_token=access_token,
          exp=exp,
          token_type="bearer"
        )
      )
    else:
      return JSONResponse(
        status_code=422,
        content=AuthErrorModel(
          message=AuthErrorTextModel.USER_ALREADY_EXISTS
        ).model_dump()
      )
  except:
    return JSONResponse(
      status_code=500,
      content=AuthErrorModel(
        message=AuthErrorTextModel.INTERNAL_SERVER_ERROR
      ).model_dump()
    )
  
# route to access api endpoints on swagger docs
@router.post(
  "/token",
  status_code=201,
  response_model=Token
)
async def login_for_access_token(
  form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
  user = await service.authenticate_user(form_data.username, form_data.password)
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect username or password",
      headers={"WWW-Authenticate": "Bearer"},
    )
  access_token, exp = create_access_token({"_id": str(user["_id"])})
  return Token(
    access_token=access_token,
    exp=exp,
    token_type="bearer"
  )