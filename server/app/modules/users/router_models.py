from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from app.models import PyObjectId
from email_validator import validate_email, EmailNotValidError
from enum import Enum

# TODO
class UserModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  username: str = Field(...)
  email: str = Field(...)
  phone: Union[None, str] = Field(None, pattern=r"^[1-9]\d{2}-\d{3}-\d{4}$")
  fullname: str = Field(...)
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
          "lastLogin": "2024-02-19T10:30:00Z",
          "huntHistory": []
        }
      ]
    }
  }

class UpdateUserModel(BaseModel):
  username: Optional[str] = Field(None)
  email: Optional[str] = Field(None, min_length=3, max_length=254) # not using a regex because email validation is relatively complex
  phone: Optional[str] = Field(None, pattern=r"^[1-9]\d{2}-\d{3}-\d{4}$")
  fullname: Optional[str] = Field(None)
  lastLogin: Optional[datetime] = Field(None)

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "username": "test",
          "email": "test@gmail.com",
          "phone": "123-456-7890",
          "fullname": "testy tester",
          "huntId": "23d3f6fccdcd5a3917558d43",
          "lastLogin": "2024-02-19T10:30:00Z"
        }
      ]
    }
  }

  @field_validator("email")
  def email_validator(cls, value):
    try:
      validate_email(value)
      return value
    except EmailNotValidError as e:
      raise ValueError("Email is not valid: " + str(e))


#enum
class UserResponseTextModel(str, Enum):
  USER_NOT_FOUND = "user not found"
  USER_FOUND = "found user"
  USER_UPDATED = "updated user"
  USER_DELETED = "deleted user"

class UserResponseModel(BaseModel):
  message: UserResponseTextModel
  content: Union[List[UserModel], UserModel, str]