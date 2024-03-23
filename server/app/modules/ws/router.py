from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.modules.ws.TeamConnectionManager import TeamConnectionManager

router = APIRouter()

manager = TeamConnectionManager()

@router.websocket("/stream")
async def websocket_endpoint(
  ws: WebSocket,
):
  await manager.connect(ws)
  try:
    while True:
      request = await ws.receive_json()
      await manager.handle_request(ws, request)
  except WebSocketDisconnect:
    await manager.disconnect(ws)