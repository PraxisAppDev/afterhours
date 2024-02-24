from fastapi import APIRouter, HTTPException
from app.modules.users.auth.service import service
from app.modules.users.auth.models import AuthResponseModel, LoginModel, SignUpModel
from app.modules.users.auth.util import create_access_token

router = APIRouter()

@router.post(
    "/login",
    status_code=201,
    response_model=AuthResponseModel
)
async def login(request: LoginModel):
  user = await service.authenticate_user(request.email, request.password)
  if user:
    await service.log_user_sign_in(user["_id"])
    return AuthResponseModel(
      message="login successful",
      token=create_access_token({"_id": str(user["_id"])})
    )
  else:
    raise HTTPException(
      status_code=422,
      detail="unable to sign in"
    )

@router.post(
  "/signup",
  status_code=201,
  response_model=AuthResponseModel
)
async def signup(request: SignUpModel):
  new_user_id = await service.create_new_user(request.username, request.email, request.fullname, request.password)
  if new_user_id:
    return AuthResponseModel(
      message="signup successful",
      token=create_access_token({"_id": new_user_id})
    )
  else:
    raise HTTPException(
      status_code=422,
      detail="unable to sign up"
    )