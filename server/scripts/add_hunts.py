import requests
from datetime import datetime
import json

class Add_Hunts():
  headers = {
      'accept': 'application/json',
      'Content-Type': 'application/json',
  }

  json_data = {
    "name": "Recruit Mixer",
    "description": "The Greene Turtle (in-person only)",
    "startDate": datetime(2024, 3, 9, 19, 0).strftime("%Y-%m-%d %I:%M %p"),
    "joinableAfterDate": datetime(2024, 3, 9, 19, 0).strftime("%Y-%m-%d %I:%M %p"),
    "endDate": datetime(2024, 5, 1, 19, 0).strftime("%Y-%m-%d %I:%M %p"),
    "huntLocation": {
      "type": "string",
      "locationName": "Greene Turtle",
      "locationInstructions": "Close to C Stone",
      "geofence": {
        "type": "string",
        "coordinates": [
          38.98086, -76.93896
        ],
        "radius": 1000
      }
    },
    "challenges": [
      {
        "questionTitle": "President",
        "description": "Who is the president of Praxis",
        "imageURL": "https://aidmelvin.github.io/personal-website/praxis_president.png",
        "placeholderText": "Type the name here:",
        "sequence": {
          "num": 1,
          "order": 1
        },
        "hints": [
          {
            "type": "string",
            "penalty": 25,
            "text": "Look on the Praxis website"
          },
          # {
          #   "type": "image",
          #   "penalty": 1,
          #   "text": "string",
          #   "imageUrl": "string"
          # }
        ],
        "scoring": {
          "points": 100,
          "timeDecay": {
            "type": "none",
            # "timeLimit": 0
          }
        },
        "response": {
          "type": "string_text_field",
          "possibleAnswers": [
            "Ashley Rush"
          ],
          "caseSensitive": False
        }
      },
      {
        "questionTitle": "CTO",
        "description": "Who is the CTO of Praxis",
        "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
        "placeholderText": "Type the name here:",
        "sequence": {
          "num": 1,
          "order": 1
        },
        "hints": [
          {
            "type": "string",
            "penalty": 25,
            "text": "Look on the Praxis website"
          },
          # {
          #   "type": "image",
          #   "penalty": 1,
          #   "text": "string",
          #   "imageUrl": "string"
          # }
        ],
        "scoring": {
          "points": 100,
          "timeDecay": {
            "type": "none",
            # "timeLimit": 0
          }
        },
        "response": {
          "type": "string_text_field",
          "possibleAnswers": [
            "Lisa Chang"
          ],
          "caseSensitive": False
        }
      }
    ],
  }

    # change("goob@gmail.com", "silly silly", "bl@hbl@h101", "raaaa raaaa")
  def do(self):
    response = requests.post('http://localhost:8001/hunts/create_hunt', headers=self.headers, json=self.json_data)
    return json.loads((response.__dict__.get('_content')).decode('utf-8')).get('inserted_hunt_id')
  


      
