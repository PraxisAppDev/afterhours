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
  elapsedTime: float = Field(...)
  answerAttempts: int = Field(...)
  score: float = Field(...)

class TeamModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  name: str = Field(...)
  teamLead: PyObjectId = Field(...)
  players: List[PyObjectId] = []
  challengeResults: List[ChallengeResultModel] = []
  isLocked: bool = Field(...)

  # TODO
  model_config = {
    "json_schema_extra": {
      "examples": [
        {
        }
      ]
    }
  }

class HuntGameStateModel(BaseModel):
  teams: List[TeamModel] = Field(...)

class HuntModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  name: str = Field(...)
  description: str = Field(...)
  startDate: datetime = Field(...)
  joinableAfterDate: datetime = Field(...)
  endDate: datetime = Field(...)
  huntLocation: dict = Field(...)
  venueLocation: List[float] = [] # Change later
  maxTeamSize: int = Field(...)
  challenges: List[dict] = Field(...)
  gameState: Optional[HuntGameStateModel] = Field(None)

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

