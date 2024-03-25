from enum import StrEnum
from typing import Dict, List
from fastapi import WebSocket
from collections import defaultdict
from pydantic import BaseModel, ConfigDict, Field
from app.modules.users.service import service as user_service
from app.modules.users.auth.service import service as auth_service

"""
EDGE CASES TO CONSIDER:
- LEADER ACCEPTS THE MOMENT JOINER LEAVES
- LEADER AND SECOND HIGHEST TENURE PLAYER BOTH LEAVE AT THE SAME TIME
"""

BUCKET_MAX_CONNECTIONS = 10

class TeamRequestType(StrEnum):
  TEAM_JOIN_REQUEST = "TEAM_JOIN_REQUEST"
  TEAM_ACCEPT_REQUEST = "TEAM_ACCEPT_REQUEST"
  TEAM_REJECT_REQUEST = "TEAM_REJECT_REQUEST"

class TeamListenerType(StrEnum):
  TEAM_INFO = "TEAMINFO"
  TEAM_JOIN_REQUESTS = "TEAM_JOIN_REQUESTS"
  TEAM_REQUEST_RESPONSES = "TEAM_REQUEST_RESPONSES"

class TeamErrorMessage(StrEnum):
  INVALID_REQUEST = "INVALID_REQUEST"
  INVALID_TOKEN = "INVALID_TOKEN"
  UPGRADE_API_VERSION = "UPGRADE_API_VERSION"
  INVALID_API_VERSION = "INVALID_API_VERSION"
  TOO_MANY_CONNECTIONS = "TOO_MANY_CONNECTIONS"

class TeamInitRole(StrEnum):
  TEAM_LEADER = "TEAM_LEADER"
  TEAM_JOINER = "TEAM_JOINER"

"""
Init Requests + Responses
"""
class InitRequestMessage(BaseModel):
  type: str = Field(default='init')
  teamId: str
  authToken: str
  role: TeamInitRole
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
  type: str = Field(default=TeamRequestType.TEAM_JOIN_REQUEST)
  joinerId: str

class TeamRequestAcceptMessage(TeamRequestBaseMessage):
  type: str = Field(default=TeamRequestType.TEAM_ACCEPT_REQUEST)
  acceptedUserId: str

class TeamRequestRejectMessage(TeamRequestBaseMessage):
  type: str = Field(default=TeamRequestType.TEAM_REJECT_REQUEST)
  rejectedUserId: str

class TeamResponseErrorMessage(BaseModel):
  errorMessage: TeamErrorMessage

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

class TeamJoinedUserInfo(BaseModel):
  username: str
  email: str
  fullname: str

type USER_ID = str

"""
TeamConnection Model
Used to avoid very large tuples
"""
class TeamConnection(BaseModel):
  # WebSocket does not have Pydantic validation...
  model_config = ConfigDict(arbitrary_types_allowed=True)

  userId: USER_ID
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

    if not response.success:
      await ws.close()

  """
  Places new websocket connection into a corresponding bucket
  TODO - VALIDATE THAT THE TEAM EXISTS
  """
  async def register_connection(self, init: InitRequestMessage, ws: WebSocket) -> InitResponseBaseMessage:
    try:
      teamId = init["teamId"]
      role = init["role"]
      authToken = init["authToken"]

      # Decrypts token here
      userId = await auth_service.get_id_with_token(authToken)

      if len(self.active_connections) > BUCKET_MAX_CONNECTIONS:
        return InitResponseFailureMessage(
          success=False,
          errorMessage=TeamErrorMessage.TOO_MANY_CONNECTIONS
        )
      elif await user_service.find_user_by_id(userId):
        listenTo = []

        if role == TeamInitRole.TEAM_JOINER:
          listenTo.append(TeamListenerType.TEAM_REQUEST_RESPONSES)
        elif role == TeamInitRole.TEAM_LEADER and not self.active_connections[teamId]:
          listenTo.append(TeamListenerType.TEAM_INFO)
          listenTo.append(TeamListenerType.TEAM_JOIN_REQUESTS)
        else:
          return InitResponseFailureMessage(
            success=False,
            errorMessage=TeamErrorMessage.INVALID_REQUEST
          )

        self.active_connections[teamId].append(TeamConnection(
          userId=userId,
          ws=ws,
          listenTo=listenTo
        ))

        # Automatically handle join request
        if role == TeamInitRole.TEAM_JOINER:
          await self.handle_join_request(ws, TeamRequestJoinMessage(
            type=TeamRequestType.TEAM_JOIN_REQUEST,
            teamId=teamId,
            joinerId=userId
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
  async def handle_request(self, ws: WebSocket, request: TeamRequestBaseMessage):
    try:
      type = request["type"]
        
      if type == TeamRequestType.TEAM_ACCEPT_REQUEST:
        await self.handle_accept_request(
          ws,
          TeamRequestAcceptMessage(
            teamId=request["teamId"],
            acceptedUserId=request["acceptedUserId"],
          )
        )
      elif type == TeamRequestType.TEAM_REJECT_REQUEST:
        await self.handle_reject_request(
          ws,
          TeamRequestRejectMessage(
            teamId=request["teamId"],
            rejectedUserId=request["rejectedUserId"],
          )
        )
      else:
        await ws.send_json(
          TeamResponseErrorMessage(
            error=TeamErrorMessage.INVALID_REQUEST
          ).model_dump()
        )

    except KeyError:
      await ws.send_json(
        TeamResponseErrorMessage(
          errorMessage=TeamErrorMessage.INVALID_REQUEST
        ).model_dump()
      )

  """
  Handles Join Request
  1. Notify team leader of join request
  """
  async def handle_join_request(self, ws: WebSocket, request: TeamRequestJoinMessage):
    teamId = request.teamId
    joinerId = request.joinerId

    if await user_service.find_user_by_id(joinerId):
      for connection in self.active_connections[teamId]:
        # Inform team leader of join request
        if TeamListenerType.TEAM_JOIN_REQUESTS in connection.listenTo:
          join_request = TeamJoinRequest(
            userId=joinerId
          )
          await connection.ws.send_json(join_request.model_dump())
  
  """
  Handles Accept Request
  1. Adds accepted user to hunt team
  2. Changes accepted user's listener from TEAMACCEPTREQUESTS to TEAMINFO
  3. Notifies joiner of acceptance
  4. Notifies everyone else in the team of the new member
  """
  async def handle_accept_request(self, ws: WebSocket, request: TeamRequestAcceptMessage):
    teamId = request.teamId
    acceptedUserId = request.acceptedUserId

    # TODO - Add HuntService method to add user to team

    # Iterates through all team member connections
    # Not costly overall since team buckets are capped at 10 connections
    for connection in self.active_connections[teamId]:
      # Inform joiner of acceptance
      if TeamListenerType.TEAM_REQUEST_RESPONSES in connection.listenTo and connection.userId == acceptedUserId:
        connection.listenTo.pop()
        connection.listenTo.append(TeamListenerType.TEAM_INFO)
            
        response = TeamJoinRequestResponse(
          success=True
        )    
        await connection.ws.send_json(response.model_dump())
          
      # Send JSON data of new user to every member on the team
      elif TeamListenerType.TEAM_INFO in connection.listenTo:
        new_member = await user_service.find_user_by_id(acceptedUserId)
        await connection.ws.send_json(TeamJoinedUserInfo(
          username=new_member["username"],
          email=new_member["email"],
          fullname=new_member["fullname"]
        ).model_dump())

  async def handle_reject_request(self, ws: WebSocket, request: TeamRequestRejectMessage):
    teamId = request.teamId
    rejectedUserId = request.rejectedUserId

    for connection in self.active_connections[teamId]:
      if TeamListenerType.TEAM_REQUEST_RESPONSES in connection.listenTo and connection.userId == rejectedUserId:
        response = TeamJoinRequestResponse(
          success=False
        )
        await connection.ws.send_json(response.model_dump())
        await connection.ws.close()

  async def disconnect(self, ws: WebSocket):
    await self.clean(ws)

  """
  Removes connection from their corresponding bucket
  """
  async def clean(self, ws: WebSocket):
    isTeamLeader = False

    for team_bucket in self.active_connections.values():
      i = 0

      while i < len(team_bucket):
        if ws == team_bucket[i].ws:
          leaveUserId = team_bucket[i].userId
          isTeamLeader = TeamListenerType.TEAM_JOIN_REQUESTS in team_bucket[i].listenTo
          break
        i += 1
      
      if i < len(team_bucket):
        # TODO - Use HuntService to remove user from team

        team_bucket.pop(i)

        for connection in team_bucket:
          if TeamListenerType.TEAM_INFO in connection.listenTo:
            await connection.ws.send_json({
              "message": "user left",
              "userId": leaveUserId
            })

        # Promote member with the longest tenure if team leader left
        # TODO - Figure out all edge cases with this
        if isTeamLeader and team_bucket:
          team_bucket[0].listenTo.append(TeamListenerType.TEAM_JOIN_REQUESTS)
          
        break
