from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field, field_validator
from app.models import PyObjectId

class TeamModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  teamname: str = Field(...)
  creation_time: datetime = Field(...)
  list_of_members: List[PyObjectId] = []
  capacity: int = Field(...)
  is_full: bool = Field(...)
  reason_full: str = Field(...)

  
  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "teamname": "testteam",
          "creationTime": "2024-02-19T10:30:00Z",
          "listOfMembers": []
        }
      ]
    }
  }


class UserCreateModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  teamname: str = Field(...)
  creation_time: datetime = Field(...)
  list_of_members: List[PyObjectId] = []

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "teamname": "testteam",
          "creationTime": "2024-02-19T10:30:00Z",
          "listOfMembers": []
        }
      ]
    }
  }

class UpdateUserModel(BaseModel):
  username: Optional[str] = Field(None)
  email: Optional[str] = Field(None, min_length=3, max_length=254) # not using a regex because email validation is relatively complex
  phone: Optional[str] = Field(None, pattern=phone_number_regex)
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

