from fastapi import APIRouter, HTTPException
from app.modules.users.auth.service import service
from app.modules.users.auth.models import LoginModel, SignUpModel

router = APIRouter()

from app.modules.users.auth.util import create_access_token

@router.post("/login")
async def login(request: LoginModel):
  user = await service.authenticate_user(request.email, request.password)
  if user:
    return {
      "message": "login successful",
      "token": create_access_token({"_id": user["_id"]})
    }
  else:
    raise HTTPException(status_code=400, detail="invalid password or email")

@router.post("/signup")
async def signup(request: SignUpModel):
  # TODO - ADD USER
  # TODO - SEND TOKEN
  return {}