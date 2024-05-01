from typing import List, Optional
from pydantic import BaseModel, Field
from app.models import PyObjectId
from datetime import datetime
from app.modules.hunts.hunt_models import ChallengeAttempt, ChallengeResult

class Player(BaseModel):
    playerId: str = Field(..., description="Player ID")
    timeJoined: datetime = Field(...)

class InitialTeamData(BaseModel):
    name: str = Field(..., min_length=1, max_length=255, description="Team name")
    is_locked: bool = Field(...)

class Team(BaseModel):
  id: str = Field(..., alias = "id")
  name: str = Field(...)
  teamLead: str = Field()
  players: List[Player] = Field()
  challengeAttempts: Optional[List[ChallengeAttempt]] = Field(None)
  challengeResults: Optional[List[ChallengeResult]] = Field(None)
  score: float = Field(..., description="Total team score")
  invitations: List[str] = Field()
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

class TeamDataWithoutInvitations(BaseModel):
    id: str = Field(..., alias = "id")
    name: str = Field(..., min_length=1, max_length=255, description="Team name")
    teamLead: str = Field(..., description="Team leader player")
    players: List[Player] = Field(...)


class TeamsResponseModel(BaseModel):
  message: str
  content: List[Team]

class TeamCreatedSuccesfully(BaseModel):
  team: Team

class TeamCreationErrorModel(BaseModel):
  error_message: str

class TeamOperationSuccessMessage(BaseModel):
  message: str

class TeamMemberRemovalSuccessModel(BaseModel):
  success: bool
  team_deleted: bool
  