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
  startDate: datetime = Field(...)
  endDate: datetime = Field(...)
  venueName: str = Field(...)
  venueLocation: List[float] = [] # Change later
  challenges: List[ChallengeModel] = []
  teams: List[TeamModel] = []

  # TODO
  model_config = {
    "json_schema_extra": {
      "examples": [
        {
        }
      ]
    }
  }

# TODO
class HuntResponseModel(BaseModel):
  message: str
  content: List[HuntModel]

class Join_Hunts_Model(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  name: str = Field(...)
  description: str = Field(...)
  huntID: str = Field(...)

  # TODO
  model_config = {
    "json_schema_extra": {
      "examples": [
        {
        }
      ]
    }
  }