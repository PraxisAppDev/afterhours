from typing import List, Optional
from pydantic import BaseModel, Field
from app.models import PyObjectId
from app.modules.hunts.router_models import ChallengeResultModel
from app.modules.users.auth.router_models import Token

class TeamModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  hunt_id: Optional[PyObjectId] = Field(alias="_id", default=None)
  name: str = Field(...)
  teamLead: PyObjectId = Field(...)
  players: List[PyObjectId] = []
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
  content: List[TeamModel]

class TeamCreatedSuccesfully(BaseModel):
  message: str
  inserted_team_id: str

class TeamCreationErrorModel(BaseModel):
  message: str
  