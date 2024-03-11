from typing import List, Optional
from pydantic import BaseModel, Field
from app.models import PyObjectId
from app.modules.hunts.router_models import ChallengeResultModel


class TeamModel(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  name: str = Field(...)
  teamLead: PyObjectId = Field(...)
  players: List[PyObjectId] = []
  challengeResults: List[ChallengeResultModel] = [0]
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
