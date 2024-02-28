from fastapi import APIRouter
from app.modules.join_hunt.service import service
from app.modules.join_hunt.router_models import Join_Hunts_Model

router = APIRouter()

@router.post(
  "/join_hunt",
  status_code=200,
  response_model=Join_Hunts_Model
)
async def load_upcoming_hunts():
  result = await service.get_upcoming()
  return Join_Hunts_Model(
    message="hunts_to_join",
    content=result
  )
