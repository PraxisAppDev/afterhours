from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(
    "/get_team_info",
    status_code=200
)
async def load_team_info():
  return[
    {
      "team_name": "Aperture Science",
      "team_members": [
        {"name": "Joe"},
        {"name": "Bob"},
        {"name": "Jim"},
        {"name": "Frank"}
      ],
      "capacity": "4",
      "is_full": "true",
      "reason_full": "capacity_reached",
    },
    {
      "team_name": "The Billy Bobs",
      "team_members": [
        {"name": "Joe"},
        {"name": "Bob"},
        {"name": "Dave"}
      ],
      "capacity": "3",
      "is_full": "false",
      "reason_full": "null",
    },
    {
      "team_name": "The Charlie Cats",
      "team_members": [
        {"name": "Joe"},
        {"name": "Bob"}
      ],
      "capacity": "4",
      "is_full": "true",
      "reason_full": "team_locked",
    },
  ]