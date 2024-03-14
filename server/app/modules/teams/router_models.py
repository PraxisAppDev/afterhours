from typing import List, Optional
from pydantic import BaseModel, Field
from app.models import PyObjectId
from app.modules.teams.team_models import Player

class TeamRequestModel(BaseModel):
  hunt_id: str = Field(...)
  name: str = Field(...)
  teamLead: str = Field()
  players: List[str] = Field()
  challengeResults: List[PyObjectId] = []
  invitations: List[str] = Field()

  # TODO
  model_config = {
    "json_schema_extra": {
      "examples": [
        {
        }
      ]
    }
  }

class TeamsResponseModel(BaseModel):
  message: str
  content: List[TeamRequestModel]

class TeamCreatedSuccesfully(BaseModel):
  message: str
  inserted_team_id: str

class TeamCreationErrorModel(BaseModel):
  message: str
  