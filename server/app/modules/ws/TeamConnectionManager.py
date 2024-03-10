import asyncio
from enum import StrEnum
import traceback
from typing import Dict, List, Union
from fastapi import WebSocket
from collections import defaultdict
from pydantic import BaseModel
from app.modules.users.service import service as user_service

type TEAM_ID = str
type USER_ID = str

class TeamRequestType(StrEnum):
  TEAMJOINREQUEST = "TEAMJOINREQUEST"
  TEAMACCEPTREQUEST = "TEAMACCEPTREQUEST"

class TeamListenerType(StrEnum):
  TEAMINFO = "TEAMINFO"
  TEAMJOINREQUESTS = "TEAMJOINREQUESTS"
  TEAMACCEPTREQUESTS = "TEAMACCEPTREQUESTS"

class TeamErrorMessage(StrEnum):
  INVALID_REQUEST = "INVALID_REQUEST"
  INVALID_TOKEN = "INVALID_TOKEN"
  UPGRADE_API_VERSION = "UPGRADE_API_VERSION"
  INVALID_API_VERSION = "INVALID_API_VERSION"

class InitRequestMessage(BaseModel):
  teamId: str
  userId: str
  listenTo: List[TeamListenerType]
  protocolExtensions: List[str]

class InitResponseBaseMessage(BaseModel):
  success: bool

class InitResponsSuccessMessage(InitResponseBaseMessage):
  protocolExtensions: List[str]

class InitReponseFailureMessage(InitResponseBaseMessage):
  errorMessage: TeamErrorMessage

class TeamRequestMessage(BaseModel):
  type: TeamRequestType
  teamId: str

class TeamRequestJoinMessage(TeamRequestMessage):
  joinerId: str

class TeamRequestAcceptMessage(TeamRequestMessage):
  acceptedUserId: str

class TeamJoinRequest(BaseModel):
  userId: str

class TeamJoinRequestResponse(BaseModel):
  success: bool

# Class that handles all the realtime logic for team operations
class TeamConnectionManager:
  def __init__(self):
    self.active_connections: Dict[
      TEAM_ID,
      List[List[Union[USER_ID, WebSocket, List[TeamListenerType]]]]
    ] = defaultdict(list)

  # Initialization of websocket connection
  async def connect(self, ws: WebSocket):
    await ws.accept()

    init = await ws.receive_json()
    self.register_connection(init, ws)

    response = InitResponsSuccessMessage(
      success=True,
      protocolExtensions=[]
    ).model_dump()

    await ws.send_json(response)

  # Places new websocket connection into a corresponding bucket
  def register_connection(self, init: InitRequestMessage, ws: WebSocket):
    teamId = init["teamId"]
    listenTo = init["listenTo"]
    userId = init["userId"]
    self.active_connections[teamId].append([userId, ws, listenTo])

  # Performs different operations based on request type
  async def handle_request(self, request: TeamRequestMessage):
    type = request["type"]
    teamId = request["teamId"]

    if type == TeamRequestType.TEAMJOINREQUEST:
      joinerId = request["joinerId"]
      
      for userId, ws, listenTo in self.active_connections[teamId]:
        # Inform team leader of join request
        if TeamListenerType.TEAMJOINREQUESTS in listenTo:
          join_request = TeamJoinRequest(
            userId=joinerId
          )
          await ws.send_json(join_request.model_dump())
    
    if type == TeamRequestType.TEAMACCEPTREQUEST:
      acceptedUserId = request["acceptedUserId"]

      # TODO - Add HuntService method to add user to team

      # Iterates through all team member connections
      # Not costly overall since teams are capped at 6 members
      for userId, ws, listenTo in self.active_connections[teamId]:
        # Inform joiner of acceptance
        if TeamListenerType.TEAMACCEPTREQUESTS in listenTo and userId == acceptedUserId:
          listenTo.pop()
          listenTo.append(TeamListenerType.TEAMINFO)
          
          response = TeamJoinRequestResponse(
            success=True
          )
          
          await ws.send_json(response.model_dump())
        
        # Send JSON data of new user to every member on the team
        elif TeamListenerType.TEAMINFO in listenTo:
          try:
            new_member = await user_service.find_user_by_id(acceptedUserId)
          except:
            new_member = {}
          
          await ws.send_json(new_member)

  # TODO - Might instead add it to a queue of connections to remove
  def disconnect(self, ws: WebSocket):
    self.clean(ws)

  # Removes connection from their corresponding bucket
  def clean(self, ws: WebSocket):
    for team_bucket in self.active_connections.values():
      i = 0

      while i < len(team_bucket):
        if ws == team_bucket[i][0]:
          break
        i += 1
      
      if i < len(team_bucket):
        team_bucket.pop(i)
        break

# import pymongo
# from app import database

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