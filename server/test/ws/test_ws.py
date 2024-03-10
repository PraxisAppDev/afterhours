import random
import string
from app.modules.ws.TeamConnectionManager import InitRequestMessage, TeamListenerType, TeamRequestAcceptMessage, TeamRequestJoinMessage, TeamRequestType
from test.client import client

# Test that connections are registered
def test_team_websocket_connection():
  with client.websocket_connect("/ws/stream") as websocket:
    payload = InitRequestMessage(
      teamId=''.join(random.choices(string.ascii_uppercase + string.digits, k=20)),
      userId=''.join(random.choices(string.ascii_uppercase + string.digits, k=20)),
      listenTo=[TeamListenerType.TEAMINFO],
      protocolExtensions=[]
    )
    websocket.send_json(payload.model_dump())
    data = websocket.receive_json()
    assert data == {
      "success": True,
      "protocolExtensions": []
    }

# Test team join request and team accept request
def test_team_websocket_join_and_accept_request():
  teamId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
  leaderId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
  joinerId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))

  with client.websocket_connect("/ws/stream") as leader:
    with client.websocket_connect("/ws/stream") as joiner:
      payload = InitRequestMessage(
        teamId=teamId,
        userId=leaderId,
        listenTo=[TeamListenerType.TEAMINFO, TeamListenerType.TEAMJOINREQUESTS],
        protocolExtensions=[]
      )
      leader.send_json(payload.model_dump())
      data = leader.receive_json()
      assert data == {
        "success": True,
        "protocolExtensions": []
      }

      payload = InitRequestMessage(
        teamId=teamId,
        userId=joinerId,
        listenTo=[TeamListenerType.TEAMACCEPTREQUESTS],
        protocolExtensions=[]
      )
      joiner.send_json(payload.model_dump())
      data = joiner.receive_json()
      assert data == {
        "success": True,
        "protocolExtensions": []
      }

      payload = TeamRequestJoinMessage(
        type=TeamRequestType.TEAMJOINREQUEST,
        teamId=teamId,
        joinerId=joinerId
      )
      joiner.send_json(payload.model_dump())

      data = leader.receive_json()
      assert data == {
        "userId": joinerId
      }

      payload = TeamRequestAcceptMessage(
        type=TeamRequestType.TEAMACCEPTREQUEST,
        teamId=teamId,
        acceptedUserId=data["userId"]
      )
      leader.send_json(payload.model_dump())

      data = joiner.receive_json()
      assert data == {
        "success": True
      }

      data = leader.receive_json()
      assert data == {}