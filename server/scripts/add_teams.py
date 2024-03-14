import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

json_data = {
    #id refers to team id, hunt_id refers to the hunt id
    "id": "",
    "hunt_id": "",
    "name": "",
    "teamLead": "",
    "players":[],
    "challengeResults": [], 
    "invitations": []
}

def change(id, hunt_id, name, teamLead, players, challenges, invitation):
    json_data['id'] = id
    json_data['hunt_id'] = hunt_id
    json_data['name'] = name
    json_data['teamLead'] = teamLead
    json_data['players'] = players
    json_data['challengeResults'] = challenges
    json_data['invitations'] = invitation

change("Team1ID", "65f235aadc9df7de117ae2fc", "BEAMTEAM", "beamer", [], [], [])
response = requests.post('http://localhost:8001/teams/create_team', headers=headers, json=json_data)

change("Team2ID", "65f235aadc9df7de117ae2fc", "DREAMTEAM", "dreamer", [], [], [])
response = requests.post('http://localhost:8001/teams/create_team', headers=headers, json=json_data)

change("Team3ID", "65ee52ace57f451f1387ea22", "CLEANTEAM", "cleaner", [], [], [])
response = requests.post('http://localhost:8001/teams/create_team', headers=headers, json=json_data)

