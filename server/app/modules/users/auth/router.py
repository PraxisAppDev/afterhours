from fastapi import APIRouter
from app.modules.users.auth.service import service
from app.modules.users.auth.models import LoginModel, SignUpModel

router = APIRouter()

@router.post("/login")
async def login(request: LoginModel):
  user = await service.authenticate_user(request.email, request.password)
  # TODO - SEND TOKEN
  return {}

@router.post("/signup")
async def signup(request: SignUpModel):
  # TODO - ADD USER
  # TODO - SEND TOKEN
  return {}