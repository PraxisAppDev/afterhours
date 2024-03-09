import random
import string
from app.modules.ws.TeamConnectionManager import TeamListenerType
from test.client import client

def test_team_websocket_connection():
  with client.websocket_connect("/ws/stream") as websocket:
    payload = {
      "teamId": ''.join(random.choices(string.ascii_uppercase + string.digits, k=20)),
      "listenerTypes": [TeamListenerType.HUNTTEAMINFO]
    }
    websocket.send_json(payload)
    data = websocket.receive_json()
    assert data == {"message": "connection established"}