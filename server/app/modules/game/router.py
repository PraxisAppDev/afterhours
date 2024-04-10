from fastapi import APIRouter
from app.modules.game.teams.router import router as teams_router
from typing_extensions import Annotated
from fastapi import Depends
from app.modules.users.auth.service import service as auth_service
from app.util import stream_jsonl_response

router = APIRouter()

router.include_router(
  teams_router,
  prefix="/{hunt_id}/teams",
)