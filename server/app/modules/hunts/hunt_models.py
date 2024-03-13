from typing import List, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from abc import ABC


# base model in case we want to add other geo options
class HuntLocation(ABC, BaseModel):
    type: str


class HuntLocationPointAndRadius(HuntLocation):
    type: str = Field(..., description="The type of geofence. Must be 'Point and Radius'")
    coordinates: List[float] = Field(
        ...,
        description="The coordinates of the center. Must have exactly 2 points, which are a pair of (longitude, latitude)"
    )
    radius: float = Field(
        ...,
        description="The radius from the center, in meters"
    )


class HuntLocationGeofence(HuntLocation):
    locationName: str = Field(..., min_length=1, max_length=255, description="Short name + address of hunt location")
    locationInstructions: Optional[str] = Field(None, min_length=1, max_length=4096, description="Instructions on how to get to hunt location")
    geofence: HuntLocationPointAndRadius = Field(
        None,
        description="The geofence that defines the area in which the hunt can be joined. If None, the hunt can be joined from anywhere."
    )


class Hint(ABC, BaseModel):
    type: str
    penalty: Optional[float]


class StringHint(Hint):
    type: str = Field("string", description="The type of clue. Must be 'string'")
    text: str = Field(..., min_length=1, max_length=32768, description="The text of the clue")
    penalty: Optional[float] = Field(None, gt=0, description="Points deducted for viewing this clue. Must be positive.")


class ImageHint(Hint):
    type: str = Field("image", description="The type of clue. Must be 'image'")
    imageUrl: str = Field(..., min_length=1, max_length=32768, description="The URL of the image")
    penalty: Optional[float] = Field(None, gt=0, description="Points deducted for viewing this clue. Must be positive.")


class NoTimeDecayScoring(BaseModel):
    type: str = Field("none", description="The type of time decay. Must be 'none'")
    timeLimit: Optional[float] = Field(None, description="Time limit in minutes. If None, no time limit.")


class LinearTimeDecayScoring(BaseModel):
    type: str = Field("linear", description="The type of time decay. Must be 'linear'")
    decayRate: float = Field(..., description="Point deduction per minute")
    timeLimit: Optional[float] = Field(None, description="Time limit in minutes. If None, decay until 0 points.")


class ExponentialTimeDecayScoring(BaseModel):
    type: str = Field("exponential", description="The type of time decay. Must be 'exponential'")
    halfLife: float = Field(..., description="Half life in seconds")
    timeLimit: Optional[float] = Field(None, description="Time limit in minutes. If None, no time limit.")


class Scoring(BaseModel):
    points: float = Field(..., description="Points awarded for solving")
    timeDecay: Union[NoTimeDecayScoring, LinearTimeDecayScoring, ExponentialTimeDecayScoring] = Field(...)


class StringResponse(BaseModel):
    type: str = Field("string_text_field", description="Response type")
    possibleAnswers: List[str] = Field(..., min_items=1, description="Possible correct answers")
    caseSensitive: bool = Field(False, description="Case sensitive matching")


class StringSetMatchedResponse(BaseModel):
    type: str = Field("string_set_matched", description="Response type")
    possibleAnswers: List[List[str]] = Field(..., min_items=1, description="Possible correct answer sets")
    caseSensitive: bool = Field(False, description="Case sensitive matching")


class MultipleChoiceResponse(BaseModel):
    type: str = Field("multiple_choice", description="Response type")
    choices: List[str] = Field(..., min_items=1, description="Choices to display")
    correctAnswers: List[int] = Field(..., min_items=1, description="Indices of correct choices")


class NumberResponse(BaseModel):
    type: str = Field("number", description="Response type")
    possibleAnswers: List[float] = Field(..., min_items=1, description="Possible correct answers")


class NumberRangeResponse(BaseModel):
    type: str = Field("number_range", description="Response type")
    minAnswer: Optional[float] = Field(None, description="Minimum value")
    maxAnswer: Optional[float] = Field(None, description="Maximum value")


class DateTimeResponse(BaseModel):
    type: str = Field("date_time", description="Response type")
    minAnswer: Optional[datetime] = Field(None, description="Earliest correct datetime")
    maxAnswer: Optional[datetime] = Field(None, description="Latest correct datetime")


class QRCodeIdResponse(BaseModel):
    type: str = Field("qr_code_id_response", description="Response type")
    correctId: str = Field(..., min_length=16, max_length=255, description="Correct QR code ID")


Response = Union[StringResponse, StringSetMatchedResponse, MultipleChoiceResponse, NumberResponse,
                 NumberRangeResponse, DateTimeResponse, QRCodeIdResponse]


class Sequence(BaseModel):
    num: int = Field(..., description="Sequence number")
    order: Optional[int] = Field(None, description="Order within sequence")


class Challenge(BaseModel):
    questionTitle: str = Field(..., min_length=1, max_length=255, description="Question title")
    description: Optional[str] = Field(None, min_length=1, max_length=32768, description="Question text")
    imageURL: str = Field(..., min_length=1, max_length=255, description="URL for Question Image")
    placeholderText: Optional[str] = Field(None, min_length=1, max_length=255, description="Text field placeholder")
    sequence: Sequence = Field(...)
    # hints: List[Hint] = Field(...)
    hints: List[Union[StringHint, ImageHint]] = Field(..., description="List of hints")
    scoring: Scoring = Field(...)
    response: Response = Field(...)


class ChallengeResult(BaseModel):
    challengeId: str = Field(..., description="Challenge ID")
    solved: datetime = Field(..., description="Time solved")
    elapsedTime: float = Field(..., description="Time to solve in seconds")
    answerAttempts: int = Field(..., description="Number of answer attempts")
    hintsViewed: int = Field(..., description="Number of hints viewed")
    pointsAwarded: float = Field(..., description="Points awarded")
    answerProvided: Optional[Union[str, None]] = Field(None, description="Last answer attempt")


class Player(BaseModel):
    playerId: str = Field(..., description="Player ID")
    timeJoined: datetime = Field(...)


class Team(BaseModel):
    id: Optional[str] = Field(None, alias="id")
    name: str = Field(..., min_length=1, max_length=255, description="Team name")
    teamLead: str = Field(..., description="Team leader player ID")
    players: List[Player] = Field(...)
    challengeResults: Optional[List[ChallengeResult]] = Field(None)
    invitations: List[str] = Field(...)


class HuntGameState(BaseModel):
    teams: List[Team] = Field(...)


class HuntSchema(BaseModel):
    id: Optional[str] = Field(None, alias="id")
    name: str = Field(..., min_length=1, max_length=255, description="Challenge name")
    description: Optional[str] = Field(None, min_length=1, max_length=4096, description="Challenge description")
    startDate: str = Field(..., description="Start date/time")
    joinableAfterDate: str = Field(..., description="Team join start date/time")
    endDate: str = Field(..., description="End date/time")
    huntLocation: HuntLocationGeofence = Field(...)
    challenges: List[Challenge] = Field(...)
    gameState: Optional[HuntGameState] = Field(None, description="Populated only during active hunt")
