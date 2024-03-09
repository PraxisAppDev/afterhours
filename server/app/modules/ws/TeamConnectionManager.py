from enum import StrEnum
import logging
from typing import Dict, List, Tuple
from fastapi import WebSocket
from collections import defaultdict

import pymongo
from app import database

# Only care about HUNTTEAMINFO & HUNTTEAMJOINREQUEST for now

class TeamRequestType(StrEnum):
  HUNTTEAMJOINREQUEST = "HUNTTEAMJOINREQUEST"
  HUNTTEAMACCEPTREQUEST = "HUNTTEAMACCEPTREQUEST"

class TeamListenerType(StrEnum):
  HUNTTEAMINFO = "HUNTTEAMINFO"
  HUNTTEAMJOINREQUESTS = "HUNTTEAMJOINREQUESTS"

type TEAM_ID = str

# class TeamDBChangeStream:
#   def __init__(self):
#     self.collection = database.get_collection("teams")
#     self.pipeline = [{ '$match': { 'operationType': ['insert', 'delete'] } }]
#     self.resume_token = None
  
#   async def watch_collection(self):
#     try:
#       # Change collection name later
#       async with self.collection.watch(self.pipeline, self.resume_token) as stream:
#         async for insert_change in stream:
#           print(insert_change)
#           self.resume_token = stream.resume_token
#     except pymongo.errors.PyMongoError:
#       if not self.resume_token:
#         logging.error('Failure in stream initialization')
#       else:
#         self.watch_collection()


class TeamConnectionManager:
  def __init__(self):
    self.active_connections: Dict[
      TEAM_ID,
      List[Tuple[WebSocket, List[TeamListenerType]]]
    ] = defaultdict(list)

  async def connect(self, ws: WebSocket):
    await ws.accept()
    init = await ws.receive_json()
    self.register_connection(init, ws)
    await ws.send_json({"message": "connection established"})

  def register_connection(self, init: object, ws: WebSocket):
    teamId = init["teamId"]
    listenerTypes = init["listenerTypes"]
    self.active_connections[teamId].append((ws, listenerTypes))

  async def handle_request(self, request: object):
    type = request["type"]

  def disconnect(self, ws: WebSocket):
    # TODO - Might instead add it to a queue of connections to remove
    self.clean(ws)
  
  def clean(self, ws: WebSocket):
    for team_bucket in self.active_connections.values():
      i = 0
      while i < len(team_bucket):
        if ws == team_bucket[i][0]:
          break
        i += 1
      if i < len(team_bucket):
        team_bucket.pop(i)