from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field
from app.models import PyObjectId
from app.modules.users.router_models import UserModel

class ClueModel(BaseModel):
  hint: str = Field(...)

class ChallengeModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  sequence: int = Field(...)
  description: str = Field(...)
  clues: List[ClueModel] = []
  difficulty: int = Field(...)
  solution: str = Field(...)

  # TODO
  model_config = {
    "json_schema_extra": {
      "examples": [
        {
        }
      ]
    }
  }

class ChallengeResultModel(BaseModel):
  challengeId: PyObjectId = Field(...)
  solved: bool = Field(...)
  elapsedTime: int = Field(...)
  answerAttempts: int = Field(...)
  score: int = Field(...)

class TeamModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  name: str = Field(...)
  teamLead: PyObjectId = Field(...)
  players: List[PyObjectId] = []
  challengeResults: List[ChallengeResultModel] = []

  # TODO
  model_config = {
    "json_schema_extra": {
      "examples": [
        {
        }
      ]
    }
  }

class HuntModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  name: str = Field(...)
  description: str = Field(...)
  # startDate: datetime = Field(...)
  # endDate: datetime = Field(...)
  startDate: str = Field(...)
  joinableAfterDate: str = Field(...)
  endDate: str = Field(...)
  huntLocation: dict = Field(...)
  # venueLocation: List[float] = [] # Change later
  # challenges: List[ChallengeModel] = []
  # teams: List[TeamModel] = []
  challenges: List[dict] = Field(...)
  teams: List[dict] = Field(...)

  # TODO
  model_config = {
    "json_schema_extra": {
      "examples": [
        {
        }
      ]
    }
  }


class HuntResponseModel(BaseModel):
  message: str
  content: List[HuntModel]


class HuntCreatedSuccessfullyModel(BaseModel):
  message: str
  inserted_hunt_id: str


class HuntCreationErrorModel(BaseModel):
  message: str 

