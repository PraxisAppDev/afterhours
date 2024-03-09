from enum import StrEnum
from typing import Dict, List
from fastapi import WebSocket
from collections import defaultdict

# Only care about HUNTTEAM & HUNTTEAMJOINREQUEST for now
class TeamRequestType(StrEnum):
  HUNTTEAMINFO = "HUNTTEAMINFO"
  HUNTTEAMJOINREQUEST = "HUNTTEAMJOINREQUEST"
  HUNTQUESTIONSTATUS = "HUNTQUESTIONSTATUS"

type TEAM_ID = str

class TeamConnectionManager:
  def __init__(self):
    self.active_connections: Dict[
      TEAM_ID,
      List[WebSocket]
    ] = defaultdict(list)

  async def connect(self, ws: WebSocket):
    await ws.accept()
    init = await ws.receive_json()
    self.register_connection(init, ws)
    await ws.send_json({"message": "connection established"})

  def register_connection(self, init: object, ws: WebSocket):
    teamId = init["teamId"]
    self.active_connections[teamId].append(ws)

  async def handle_request(self, request: object):
    type = request["type"]

  def disconnect(self, ws: WebSocket):
    # TODO - Might instead add it to a queue of connections to remove
    self.clean(ws)
  
  def clean(self, ws):
    for team_bucket in self.active_connections.values():
      if ws in team_bucket:
        team_bucket.remove(ws)