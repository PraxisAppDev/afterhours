from fastapi import APIRouter, HTTPException
from app.modules.users.service import service
from app.modules.users.auth import router as auth
from app.modules.users.models import UserModel, UserResponseModel

router = APIRouter()

router.include_router(
    auth.router,
    prefix="/auth",
)

@router.get("/")
async def read_users(
  status_code=200,
  response_model=UserResponseModel
):
  result = await service.get_users()
  return UserResponseModel(
    message="fetched users",
    content=result
  )

@router.get("/{id}")
async def find_user_by_id(
  id: str,
  status_code=200,
  response_model=UserResponseModel
):
  result = await service.find_user_by_id(id)
  if result:
    return UserResponseModel(
      message="found user",
      content=result
    )
  else:
    raise HTTPException(status_code=400, detail="user not found")

@router.get("/email/{email}")
async def find_user_by_email(
  email: str,
  status_code=200,
  response_model=UserResponseModel
):
  result = await service.find_user_by_email(email)
  if result:
    return UserResponseModel(
      message="found user",
      content=result
    )
  else:
    raise HTTPException(status_code=400, detail="user not found")

@router.post("/add")
async def add_user(
  user: UserModel,
  status_code = 201,
  response_model=UserResponseModel
):
  result = await service.add_user(user)
  if result:
    return UserResponseModel(
      message="successfully created user",
      content=result
    )
  else:
    raise HTTPException(status_code=409, detail="user already exists")

@router.put("/{id}")
async def update_user_by_id(
  id,
  user: UserModel,
  status_code = 200,
  response_model=UserResponseModel
):
  result = await service.update_user_by_id(id, user)
  if result:
    return UserResponseModel(
      message="successfully updated user",
      content=result
    )
  else:
    raise HTTPException(status_code=400, detail="user does not exist")

@router.delete("/{id}")
async def delete_user_by_id(
  id,
  status_code=200,
  response_model=UserResponseModel
):
  result = await service.delete_user_by_id(id)
  if result:
    return UserResponseModel(
      message="successfully deleted user",
      content=result
    )
  else:
    raise HTTPException(status_code=400, detail="user not found")