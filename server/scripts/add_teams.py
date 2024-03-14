import requests
from json import dumps

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

def change( hunt_id, name, teamLead, players, invitation):
    json_data['hunt_id'] = hunt_id
    json_data['name'] = name
    json_data['teamLead'] = teamLead
    json_data['players'] = players
    json_data['invitations'] = invitation

#Players = [{"65e8d7479bf978a5b7c2dfbb", "timeJoined": datetime.now().strftime("%Y-%m-%d %I:%M %p")},]
change("65f38146d727b5919ed168ab", "BEAMTEAM", "65e8d7479bf978a5b7c2dfbb", [], [])
response = requests.post('http://localhost:8001/teams/create_team', headers=headers, json=json_data)

#Players = [{"65e8d8d29bf978a5b7c2dfbc", "timeJoined": datetime.now().strftime("%Y-%m-%d %I:%M %p")},]
change("65f38146d727b5919ed168ab", "DREAMTEAM", "65e8d8d29bf978a5b7c2dfbc", [], [])
response = requests.post('http://localhost:8001/teams/create_team', headers=headers, json=json_data)

