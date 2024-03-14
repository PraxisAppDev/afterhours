from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.modules.hunts.hunt_models import ChallengeResult 

class Player(BaseModel):
    playerId: str = Field(..., description="Player ID")
    timeJoined: datetime = Field(...)

class Team(BaseModel):
    hunt_id: str = Field(None, alias = "hunt_id")
    name: str = Field(..., min_length=1, max_length=255, description="Team name")
    teamLead: Player = Field(..., description="Team leader player")
    players: List[Player] = Field(...)
    challengeResults: Optional[List[ChallengeResult]] = Field(None)
    invitations: List[str] = Field(...)
