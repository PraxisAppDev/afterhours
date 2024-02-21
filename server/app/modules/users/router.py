from fastapi import APIRouter, HTTPException
from app.modules.users.service import service
from app.modules.users.auth import router as auth
from app.modules.users.models import UpdateUserModel, UserModel, UserResponseModel

router = APIRouter()

router.include_router(
    auth.router,
    prefix="/auth",
)

@router.get(
  "/",
  response_model=UserResponseModel,
  status_code=200
)
async def read_users():
  result = await service.get_users()
  return UserResponseModel(
    message="fetched users",
    content=result
  )

@router.get(
  "/{id}",
  status_code=200,
  response_model=UserResponseModel
)
async def find_user_by_id(id: str):
  result = await service.find_user_by_id(id)
  if result:
    return UserResponseModel(
      message="found user",
      content=result
    )
  else:
    raise HTTPException(status_code=400, detail="user not found")

@router.get(
  "/email/{email}",
  status_code=200,
  response_model=UserResponseModel
)
async def find_user_by_email(email: str):
  result = await service.find_user_by_email(email)
  if result:
    return UserResponseModel(
      message="found user",
      content=result
    )
  else:
    raise HTTPException(status_code=400, detail="user not found")
  
@router.get(
  "/username/{username}",
  status_code=200,
  response_model=UserResponseModel
)
async def find_user_by_username(username: str):
  result = await service.find_user_by_username(username)
  if result:
    return UserResponseModel(
      message="found user",
      content=result
    )
  else:
    raise HTTPException(status_code=400, detail="user not found")

@router.post(
  "/add",
  status_code = 201,
  response_model=UserResponseModel
)
async def add_user(user: UserModel):
  result = await service.add_user(user)
  if result:
    return UserResponseModel(
      message="successfully created user",
      content=result
    )
  else:
    raise HTTPException(status_code=409, detail="user already exists")

@router.put(
  "/{id}",
  status_code = 200,
  response_model=UserResponseModel
)
async def update_user_by_id(id, user: UpdateUserModel):
  result = await service.update_user_by_id(id, user)
  if result:
    return UserResponseModel(
      message="successfully updated user",
      content=result
    )
  else:
    raise HTTPException(status_code=400, detail="user does not exist")

@router.delete(
  "/{id}",
  status_code=200,
  response_model=UserResponseModel
)
async def delete_user_by_id(id):
  result = await service.delete_user_by_id(id)
  if result:
    return UserResponseModel(
      message="successfully deleted user",
      content=result
    )
  else:
    raise HTTPException(status_code=400, detail="user not found")