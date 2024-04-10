import requests
from json import dumps
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
import sys
sys.path.append('../')

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
        "invitations": [],
        "isLocked": False
    }

    def change(self, name, teamLead, players, invitation, isLocked):
        self.json_data['name'] = name
        self.json_data['teamLead'] = teamLead
        self.json_data['players'] = players
        self.json_data['isLocked'] = isLocked
        self.json_data['invitations'] = invitation
        
        

    def add(self, hunt_id, team_id):
        requests.post('http://localhost:8001/users/auth/login', headers=self.headers)

        #Players = [{"65e8d7479bf978a5b7c2dfbb", "timeJoined": datetime.now().strftime("%Y-%m-%d %I:%M %p")},]
        self.change(hunt_id, "BEAMTEAM", "Jim Jones", ["Jim Jones", "Bob Smith"], [], False)
        requests.post('http://localhost:8001/teams/create_team', headers=self.headers, json=self.json_data)

        #Players = [{"65e8d8d29bf978a5b7c2dfbc", "timeJoined": datetime.now().strftime("%Y-%m-%d %I:%M %p")},]
        self.change(hunt_id, "DREAMTEAM", "Jim Jones", ["Jim Jones", "Bob Smith", "Tom Donaldson"], [], True)
        requests.post('http://localhost:8001/teams/create_team', headers=self.headers, json=self.json_data)

        

