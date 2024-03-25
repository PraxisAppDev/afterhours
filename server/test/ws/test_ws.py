import asyncio
import random
import string
import pytest
from app.modules.ws.TeamConnectionManager import InitRequestMessage, TeamRequestAcceptMessage, TeamRequestType
from test.client import client
from app.database import database

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

json_data = {
    'email': '',
    'fullname': '',
    'password': '',
    'username': '',
}

def change(email, fullname, password, username):
    json_data['email'] = email
    json_data['fullname'] = fullname
    json_data['password'] = password
    json_data['username'] = username
    
userTokens = []

def initialize_data():
  loop = asyncio.get_event_loop()
  loop.run_until_complete(database.get_collection("users").delete_many({}))
  change("leader@gmail.com", "leaderleader", "leaderleader123$", "leaderleader")
  response = client.post("/users/auth/signup", headers=headers, json=json_data)
  userTokens.append(response.json()["token"]["access_token"])
  change("joiner@gmail.com", "joinerjoiner", "joinerjoiner123$", "joinerjoiner")
  response = client.post("/users/auth/signup", headers=headers, json=json_data)
  userTokens.append(response.json()["token"]["access_token"])

initialize_data()

"""
Test that connections are registered
"""
def test_team_websocket_connection():
  with client.websocket_connect("/ws/stream") as websocket:
    payload = InitRequestMessage(
      teamId=''.join(random.choices(string.ascii_uppercase + string.digits, k=20)),
      authToken=userTokens[1],
      role="TEAM_LEADER",
      protocolExtensions=[]
    )
    websocket.send_json(payload.model_dump())
    data = websocket.receive_json()
    assert data == {
      "type": "initResponse",
      "success": True,
      "protocolExtensions": []
    }

"""
Test team join request and team accept request
"""
@pytest.mark.timeout(3)
def test_team_websocket_join_and_accept_request():
  teamId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
  leaderToken = userTokens[0]
  joinerToken = userTokens[1]

  with client.websocket_connect("/ws/stream") as leader:
    with client.websocket_connect("/ws/stream") as joiner:
      payload = InitRequestMessage(
        teamId=teamId,
        authToken=leaderToken,
        role="TEAM_LEADER",
        protocolExtensions=[]
      )
      leader.send_json(payload.model_dump())
      data = leader.receive_json()
      assert data == {
        "type": "initResponse",
        "success": True,
        "protocolExtensions": []
      }

      payload = InitRequestMessage(
        teamId=teamId,
        authToken=joinerToken,
        role="TEAM_JOINER",
        protocolExtensions=[]
      )
      joiner.send_json(payload.model_dump())
      data = joiner.receive_json()
      assert data == {
        "type": "initResponse",
        "success": True,
        "protocolExtensions": []
      }

      data = leader.receive_json()

      assert "userId" in data

      payload = TeamRequestAcceptMessage(
        type=TeamRequestType.TEAM_ACCEPT_REQUEST,
        teamId=teamId,
        acceptedUserId=data["userId"]
      )
      leader.send_json(payload.model_dump())

      data = leader.receive_json()
      assert data == {
        "username": "joinerjoiner",
        "email": "joiner@gmail.com",
        "fullname": "joinerjoiner"
      }

"""
Tests if team members get notified if a user leaves
(DID THIS MANUALLY INSTEAD)
"""
def test_team_websocket_leave():
  pass
  # teamId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
  # leaderToken = userTokens[0]
  # joinerToken = userTokens[1]

  # with client.websocket_connect("/ws/stream") as leader:
  #   with client.websocket_connect("/ws/stream") as joiner:
  #     payload = InitRequestMessage(
  #       teamId=teamId,
  #       authToken=leaderToken,
  #       role="TEAM_LEADER",
  #       protocolExtensions=[]
  #     )
  #     leader.send_json(payload.model_dump())
  #     data = leader.receive_json()
  #     assert data == {
  #       "type": "initResponse",
  #       "success": True,
  #       "protocolExtensions": []
  #     }

  #     payload = InitRequestMessage(
  #       teamId=teamId,
  #       authToken=joinerToken,
  #       role="TEAM_JOINER",
  #       protocolExtensions=[]
  #     )
  #     joiner.send_json(payload.model_dump())
  #     data = joiner.receive_json()
  #     assert data == {
  #       "type": "initResponse",
  #       "success": True,
  #       "protocolExtensions": []
  #     }
      
    # member.close()
    
    # data = leader.receive_json()
    # assert data == {
    #   "message": "user left",
    #   "userId": memberId
    # }