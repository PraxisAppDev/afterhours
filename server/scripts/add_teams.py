import requests
from json import dumps
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
import sys
sys.path.append('../')

class Add_Teams:
    def __init__(self) -> None:
        self.token = ''
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}',
        }

        self.json_data = {
            #id refers to team id, hunt_id refers to the hunt id
            "hunt_id": "",
            "team": "",
            "name": "",
            "isLocked" : False
        }

    def change(self, huntId, teamName, isLocked):
        self.json_data['hunt_id'] = huntId
        self.json_data['team'] = {'name': teamName}
        self.json_data['name'] = teamName
        self.json_data['isLocked'] = isLocked
        

    def add(self, hunt_ids):
        data = [
            ('looneys', 'strawberry+martini2', 'BEAMTEAM'),
            ('Rosserson', 'Pheobe4ever!', 'Test Team 2'),
            ('newman', 'george*costanza4', 'Test Team 3'),
            ('brownies', 'Boba:)100', 'Test Team 4')
        ]
        i = 0
        for username, password, teamName in data:
            response = requests.post('http://localhost:8001/users/auth/login', headers=self.headers, json={'username': username, 'password': password}).json()
            self.token = response['token']['access_token']

            # IMPORTANT: this needs to be updated or else it won't have the token
            # after it's updated
            self.headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.token}',
            }

            self.change(hunt_ids[i], teamName, False)
            requests.post(f'http://localhost:8001/game/{hunt_ids[i]}/teams/create_team', headers=self.headers, json=self.json_data)
            i = i + 1
