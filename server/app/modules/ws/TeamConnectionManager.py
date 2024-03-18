from enum import StrEnum
from typing import Dict, List
from fastapi import WebSocket
from collections import defaultdict
from pydantic import BaseModel, ConfigDict, Field
from app.modules.users.service import service as user_service
from app.modules.users.auth.service import service as auth_service

class TeamRequestType(StrEnum):
  TEAMJOINREQUEST = "TEAMJOINREQUEST"
  TEAMACCEPTREQUEST = "TEAMACCEPTREQUEST"
  ADDLISTENER = "ADDLISTENER"

class TeamListenerType(StrEnum):
  TEAMINFO = "TEAMINFO"
  TEAMJOINREQUESTS = "TEAMJOINREQUESTS"
  TEAMACCEPTREQUESTS = "TEAMACCEPTREQUESTS"

class TeamErrorMessage(StrEnum):
  INVALID_REQUEST = "INVALID_REQUEST"
  INVALID_TOKEN = "INVALID_TOKEN"
  UPGRADE_API_VERSION = "UPGRADE_API_VERSION"
  INVALID_API_VERSION = "INVALID_API_VERSION"

"""
Init Requests + Responses
"""
class InitRequestMessage(BaseModel):
  type: str = Field(default='init')
  teamId: str
  # userId: str
  authToken: str
  listenTo: List[TeamListenerType]
  protocolExtensions: List[str]

class InitResponseBaseMessage(BaseModel):
  type: str = Field(default='initResponse')
  success: bool

class InitResponseSuccessMessage(InitResponseBaseMessage):
  protocolExtensions: List[str]

class InitResponseFailureMessage(InitResponseBaseMessage):
  errorMessage: TeamErrorMessage

"""
Team Requests + Responses
"""
class TeamRequestBaseMessage(BaseModel):
  type: TeamRequestType
  teamId: str

class TeamRequestJoinMessage(TeamRequestBaseMessage):
  authToken: str

class TeamRequestAcceptMessage(TeamRequestBaseMessage):
  acceptedUserId: str

"""
Reactionary Models
Pushed to specific websockets as a "reaction" to other websocket requests
For example, if one connection makes a TeamRequestJoinMessage to the manager,
we would then send a TeamJoinRequest to the specific team leader
"""
class TeamJoinRequest(BaseModel):
  userId: str

class TeamJoinRequestResponse(BaseModel):
  success: bool

"""
TeamConnection Model
Used to avoid very large tuples
"""
class TeamConnection(BaseModel):
  # WebSocket does not have Pydantic validation...
  model_config = ConfigDict(arbitrary_types_allowed=True)

  userId: str
  ws: WebSocket
  listenTo: List[TeamListenerType]

type TEAM_ID = str

"""
TeamConnectionManager
Class that handles all the realtime logic for team operations
"""
class TeamConnectionManager:
  def __init__(self):
    self.active_connections: Dict[
      TEAM_ID,
      List[TeamConnection]
    ] = defaultdict(list)

  """
  Initialization of websocket connection
  """
  async def connect(self, ws: WebSocket):
    await ws.accept()

    init = await ws.receive_json()
    
    response = await self.register_connection(init, ws)

    await ws.send_json(response.model_dump())

  """
  Places new websocket connection into a corresponding bucket
  """
  async def register_connection(self, init: InitRequestMessage, ws: WebSocket) -> InitResponseBaseMessage:
    try:
      teamId = init["teamId"]
      listenTo = init["listenTo"]
      authToken = init["authToken"]

      # Decrypts token here
      userId = await auth_service.get_id_with_token(authToken)

      if await user_service.find_user_by_id(id):
        self.active_connections[teamId].append(TeamConnection(
          userId=userId,
          ws=ws,
          listenTo=listenTo
        ))
        return InitResponseSuccessMessage(
          success=True,
          protocolExtensions=[]
        )
    
      else:
        return InitResponseFailureMessage(
          success=False,
          errorMessage=TeamErrorMessage.INVALID_TOKEN
        )
      
    except KeyError:
      return InitResponseFailureMessage(
        success=False,
        errorMessage=TeamErrorMessage.INVALID_REQUEST
      )

  """
  Performs different methods based on request type
  """
  async def handle_request(self, request: TeamRequestBaseMessage):
    type = request["type"]

    if type == TeamRequestType.TEAMJOINREQUEST:
      await self.handle_join_request(request)
      
    elif type == TeamRequestType.TEAMACCEPTREQUEST:
      await self.handle_accept_request(request)

  """
  Handles Join Request
  1. Validates request (TODO)
  2. Notify team leader of join request
  """
  async def handle_join_request(self, request: TeamRequestJoinMessage):
    teamId = request["teamId"]
    # TODO - Maybe find a way to not need an authToken
    authToken = request["authToken"]
    joinerId = await auth_service.get_id_with_token(authToken)

    if await user_service.find_user_by_id(id):
      for connection in self.active_connections[teamId]:
        # Inform team leader of join request
        if TeamListenerType.TEAMJOINREQUESTS in connection.listenTo:
          join_request = TeamJoinRequest(
            userId=joinerId
          )
          await connection.ws.send_json(join_request.model_dump())
  
  """
  Handles Accept Request
  1. Validates request (TODO)
  2. Adds accepted user to hunt team
  3. Changes accepted user's listener from TEAMACCEPTREQUESTS to TEAMINFO
  4. Notifies joiner of acceptance
  5. Notifies everyone else in the team of the new member
  """
  async def handle_accept_request(self, request: TeamRequestAcceptMessage):
    teamId = request["teamId"]
    acceptedUserId = request["acceptedUserId"]

    # TODO - Add HuntService method to add user to team

    # Iterates through all team member connections
    # Not costly overall since teams are capped at 6 members
    for connection in self.active_connections[teamId]:
      # Inform joiner of acceptance
      if TeamListenerType.TEAMACCEPTREQUESTS in connection.listenTo and connection.userId == acceptedUserId:
        connection.listenTo.pop()
        connection.listenTo.append(TeamListenerType.TEAMINFO)
            
        response = TeamJoinRequestResponse(
          success=True
        )    
        await connection.ws.send_json(response.model_dump())
          
      # Send JSON data of new user to every member on the team
      elif TeamListenerType.TEAMINFO in connection.listenTo:
        # try except is for testing purposes, can remove later
        try:
          new_member = await user_service.find_user_by_id(acceptedUserId)
        except:
          new_member = {}

        await connection.ws.send_json(new_member)

  def disconnect(self, ws: WebSocket):
    self.clean(ws)

  """
  Removes connection from their corresponding bucket
  """
  def clean(self, ws: WebSocket):
    for team_bucket in self.active_connections.values():
      i = 0

      while i < len(team_bucket):
        if ws == team_bucket[i].ws:
          leaveUserId = team_bucket[i].userId
          isTeamLeader = TeamListenerType.TEAMJOINREQUESTS in team_bucket[i].listenTo
          break
        i += 1
      
      if i < len(team_bucket):
        # TODO - Use HuntService to remove user from team

        team_bucket.pop(i)

        for connection in team_bucket:
          # TODO Change message
          connection.ws.send_json({
            "message": "user left",
            "userId": leaveUserId
          })

        # Promote member with the longest tenure if team leader left
        # TODO - Figure out all edge cases with this
        if isTeamLeader and team_bucket:
          team_bucket[0].listenTo.append(TeamListenerType.TEAMJOINREQUESTS)
          
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