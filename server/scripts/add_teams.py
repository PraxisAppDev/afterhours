import requests
from json import dumps
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
import sys
sys.path.append('../')
from app import database
from bson import ObjectId

class Add_Teams:
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        #id refers to team id, hunt_id refers to the hunt id
        "hunt_id": "",
        "name": "",
        "teamLead": "",
        "players":[],
        "invitations": []
    }
    class hunter:
        def __init__(self):
            self.collection = database.get_collection("hunts")

        def find_hunt_id(self):
            hunt_id = self.collection.find({
            "_id": { }
            })
            return hunt_id

    def change(self,hunt_id, name, teamLead, players, invitation):
        self.json_data['hunt_id'] = hunt_id
        self.json_data['name'] = name
        self.json_data['teamLead'] = teamLead
        self.json_data['players'] = players
        self.json_data['invitations'] = invitation

    def add(self, hunt_id, team_id):
        #Players = [{"65e8d7479bf978a5b7c2dfbb", "timeJoined": datetime.now().strftime("%Y-%m-%d %I:%M %p")},]
        self.change(hunt_id, "BEAMTEAM", "65e8d7479bf978a5b7c2dfbb", [], [])
        response = requests.post('http://localhost:8001/teams/create_team', headers=self.headers, json=self.json_data)

        #Players = [{"65e8d8d29bf978a5b7c2dfbc", "timeJoined": datetime.now().strftime("%Y-%m-%d %I:%M %p")},]
        self.change(hunt_id, "DREAMTEAM", team_id, [], [])
        response = requests.post('http://localhost:8001/teams/create_team', headers=self.headers, json=self.json_data)

