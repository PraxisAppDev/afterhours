from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field
from app.models import PyObjectId

# TODO
class UserModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  username: str = Field(...)
  email: str = Field(..., pattern=r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
  phone: Union[None, str] = Field(None, pattern=r"^[1-9]\d{2}-\d{3}-\d{4}$")
  fullname: str = Field(...)
  hashedPassword: str = Field(...)
  lastLogin: datetime = Field(...)
  huntHistory: List[PyObjectId] = []

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "username": "test",
          "email": "test@gmail.com",
          "phone": "123-456-7890",
          "fullname": "testy tester",
          "salt": "421fsd",
          "hashedPassword": "randomlyhashedpassword",
          "lastLogin": "2024-02-19T10:30:00Z",
          "huntHistory": []
        }
      ]
    }
  }

class UpdateUserModel(BaseModel):
  username: Optional[str] = Field(None)
  email: Optional[str] = Field(None, pattern=r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
  phone: Optional[str] = Field(None, pattern=r"^[1-9]\d{2}-\d{3}-\d{4}$")
  fullname: Optional[str] = Field(None)
  hashedPassword: Optional[str] = Field(None)
  lastLogin: Optional[datetime] = Field(None)

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "username": "test",
          "email": "test@gmail.com",
          "phone": "123-456-7890",
          "fullname": "testy tester",
          "hashedPassword": "randomlyhashedpassword",
          "huntId": "23d3f6fccdcd5a3917558d43",
          "lastLogin": "2024-02-19T10:30:00Z"
        }
      ]
    }
  }

class UserResponseModel(BaseModel):
  message: str
  content: Union[List[UserModel], UserModel, str]