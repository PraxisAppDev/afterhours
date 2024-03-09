import random
import string
from test.client import client

def test_team_websocket_connection():
  with client.websocket_connect("/ws/stream") as websocket:
    payload = {
      "teamId": ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
    }
    websocket.send_json(payload)
    data = websocket.receive_json()
    assert data == {"message": "connection established"}