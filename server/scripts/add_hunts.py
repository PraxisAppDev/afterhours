import requests
from datetime import datetime
import json


class Add_Hunts():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    hunt1_json = {
        "name": "Sample Hunt 1 ",
        "description": "The Greene Turtle (in-person only)",
        "startDate": datetime(2024, 3, 9, 19, 0).isoformat(),
        "joinableAfterDate": datetime(2024, 3, 9, 19, 0).isoformat(),
        "endDate": datetime(2024, 5, 1, 19, 0).isoformat(),
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
        "maxTeamSize": 4,
        "challenges": [
            {
                "id": "test1",
                "questionTitle": "Parent Organization",
                "description": "Who is the parent organization of Praxis?",
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
                        "General Dynamics",
                        "General Dynamics Corporation",
                        "General Dynamics Information Technology"
                    ],
                    "caseSensitive": False
                }
            },
            {
                "id": "test2",
                "questionTitle": "Praxis Founding Year",
                "description": "When was Praxis founded?",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type the year here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Look at the Praxis Website"
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
                    "type": "number",
                    "possibleAnswers": [
                        2002
                    ],
                    "caseSensitive": False
                }
            },
            {
                "id": "test3",
                "questionTitle": "Core Values",
                "description": "Name 3 core values of Praxis",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_president.png",
                "placeholderText": "Type the core values here:",
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
                    "type": "string_set_matched",
                    "possibleAnswers": [
                        "Customer Success",
                        "Employee Success",
                        "Technical Excellence",
                        "Fiscal Responsibility",
                        "Social Awareness"
                    ],
                    "caseSensitive": False,
                    "numOfAnswers": 3
                }
            },
            {
                "id": "test4",
                "questionTitle": "Director of Security",
                "description": "Who is the director of security at Praxis?",
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
                        "Antoinette Thomas",
                        "Antoinette"
                    ],
                    "caseSensitive": False
                }
            },
            {
                "id": "test5",
                "questionTitle": "Praxis Definition",
                "description": "Define Praxis as it relates to our company",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_president.png",
                "placeholderText": "Type the definition here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Look on the Praxis homepage"
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
                        "THE PRACTICAL APPLICATION OR EXERCISE OF A BRANCH OF LEARNING."
                        "Exercise of a branch of learning",
                        "practical application of a branch of learning"
                    ],
                    "caseSensitive": False
                }
            },
        ],
        "teams": []
    }

    hunt2_json = {
        "name": "Recruit Mixer 1",
        "description": "The Greene Turtle (in-person only)",
        "startDate": datetime(2024, 3, 9, 19, 0).isoformat(),
        "joinableAfterDate": datetime(2024, 3, 9, 19, 0).isoformat(),
        "endDate": datetime(2024, 5, 1, 19, 0).isoformat(),
        
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
        "maxTeamSize": 5,
        "challenges": [
            {
                "id": "test1",
                "questionTitle": "Find the President",
                "description": "Take a picture with the president of Praxis",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_president.png",
                "placeholderText": "Upload the image here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "image",
                        "penalty": 25,
                        "text": "This is the President",
                        "imageUrl": "img"
                    },
                ],
                "scoring": {
                    "points": 100,
                    "timeDecay": {
                        "type": "none",
                        # "timeLimit": 0
                    }
                },
                "response": {
                    "type": "img",
                    "possibleAnswers": [
                        "Ashley Rush"  # Image Checker here
                    ],
                    "caseSensitive": False
                }
            },
            {
                "id": "test2",
                "questionTitle": "Bread and Butter",
                "description": "What is the Bread and Butter of Praxis",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type your answer here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Starts with an S and ends with an E"
                    },
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
                        "Software"
                    ],
                    "caseSensitive": False
                }
            },
            {
                "id": "test3",
                "questionTitle": "Finish the sentence",
                "description": "At Praxis, our success is your ...",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type your one-word answer here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Starts with an S and ends with an E"
                    },
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
                        "Success"
                    ],
                    "caseSensitive": False
                }
            },
            {
                "id": "test4",
                "questionTitle": "Number of Employees at Praxis",
                "description": "How many employees does Praxis Engineering have at a minimum?",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type your numeric answer here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Look at our about page"
                    },
                ],
                "scoring": {
                    "points": 100,
                    "timeDecay": {
                        "type": "none",
                        # "timeLimit": 0
                    }
                },
                "response": {
                    "type": "number",
                    "possibleAnswers": [
                        350
                    ],
                    "caseSensitive": False
                }
            },
            {
                "id": "test5",
                "questionTitle": "Areas of Expertise",
                "description": "Name 3 areas in which Praxis has expertise",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type your answers here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Look at our about page"
                    },
                ],
                "scoring": {
                    "points": 100,
                    "timeDecay": {
                        "type": "none",
                        # "timeLimit": 0
                    }
                },
                "response": {
                    "type": "string_set_matched",
                    "possibleAnswers": [
                        "Software",
                        "Cybersecurity",
                        "Cyber Network Operations",
                        "Data Science",
                        "AI",
                        "Artificial Intelligence",
                        "Machine Learning",
                        "ML",
                        "High performance computing",
                        "Advanced Research",
                        "Devops",
                        "Cloud",
                        "Containers",
                        "C5ISR",
                        "Wireless Exploitation"
                    ],
                    "caseSensitive": False,
                    "numOfAnswers": 3
                }
            },
        ],
        "teams": []
    }

    hunt3_json = {
        "name": "Recruit Mixer 2",
        "description": "The Greene Turtle (in-person only)",
        "startDate": datetime(2024, 3, 9, 19, 0).isoformat(),
        "joinableAfterDate": datetime(2024, 3, 9, 19, 0).isoformat(),
        "endDate": datetime(2024, 5, 1, 19, 0).isoformat(),
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
        "maxTeamSize": 4,
        "challenges": [
            {
                "id": "test1",
                "questionTitle": "Find the Director of IT",
                "description": "Take a picture with the Director of IT",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_president.png",
                "placeholderText": "Upload the image here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "image",
                        "penalty": 25,
                        "text": "This is the Director of IT",
                        "imageUrl": "img"
                    },
                ],
                "scoring": {
                    "points": 100,
                    "timeDecay": {
                        "type": "none",
                        # "timeLimit": 0
                    }
                },
                "response": {
                    "type": "img",
                    "possibleAnswers": [
                        "Mike Schepers"  # Image Checker here
                    ],
                    "caseSensitive": False
                }
            },
            {
                "id": "test2",
                "questionTitle": "Praxis Customers",
                "description": "Name 3 customers of Praxis (acronyms)",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type your answer here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Security, Secret Agents, Defense"
                    },
                ],
                "scoring": {
                    "points": 100,
                    "timeDecay": {
                        "type": "none",
                        # "timeLimit": 0
                    }
                },
                "response": {
                    "type": "string_set_matched",
                    "possibleAnswers": [
                        "NSA",
                        "CIA",
                        "DOD"
                    ],
                    "caseSensitive": False, 
                    "numOfAnswers": 3
                }
            },
            {
                "id": "test3",
                "questionTitle": "Figure out the missing word",
                "description": "At Praxis, we are ... focused",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type your one-word answer here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "We call a journey to the moon a ..."
                    },
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
                        "mission"
                    ],
                    "caseSensitive": False
                }
            },
            {
                "id": "test4",
                "questionTitle": "Number of Contracts",
                "description": "Praxis has over ... active contracts",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type your numeric answer here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Look at our website"
                    },
                ],
                "scoring": {
                    "points": 100,
                    "timeDecay": {
                        "type": "none",
                        # "timeLimit": 0
                    }
                },
                "response": {
                    "type": "number",
                    "possibleAnswers": [
                        50
                    ],
                    "caseSensitive": False
                }
            },
            {
                "id": "test5",
                "questionTitle": "Why Praxis",
                "description": "Name 3 benefits of Praxis",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type your answers here, seperated by a comma: ",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Look at our why page titles"
                    },
                ],
                "scoring": {
                    "points": 100,
                    "timeDecay": {
                        "type": "none",
                        # "timeLimit": 0
                    }
                },
                "response": {
                    "type": "string_set_matched",
                    "possibleAnswers": [
                        "Let your voice be heard",
                        "Grow your geek",
                        "It's all about the balance",
                        "Less is more? Since when!",
                        "Whole self health"
                    ],
                    "caseSensitive": False, 
                    "numOfAnswers": 3
                }
            },
        ],
        "teams": []
    }

    hunt4_json = {
        "name": "Recruit Mixer",
        "description": "The Greene Turtle (in-person only)",
        "startDate": datetime(2024, 3, 9, 19, 0).isoformat(),
        "joinableAfterDate": datetime(2024, 3, 9, 19, 0).isoformat(),
        "endDate": datetime(2024, 5, 1, 19, 0).isoformat(),
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
        "maxTeamSize": 3,
        "challenges": [
            {
                "id": "test1",
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
                "id": "test2",
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
        "teams": []
    }

    #Warning: Sample Hunt 5's images don't match the question.
    #Sample Hunt 5 tests answers that weren't tested in the previous hunts including 
    #multiple choice, number range, and date_time
    hunt5_json = {
        "name": "Sample Hunt 5 ",
        "description": "CStone (in-person only)",
        "startDate": datetime(2024, 5, 6, 19, 0).isoformat(),
        "joinableAfterDate": datetime(2024, 5, 6, 19, 0).isoformat(),
        "endDate": datetime(2024, 5, 1, 19, 0).isoformat(),
        "huntLocation": {
            "type": "string",
            "locationName": "Cornerstone",
            "locationInstructions": "Close to Nando's",
            "geofence": {
                "type": "string",
                "coordinates": [
                    38.98086, -76.93896
                ],
                "radius": 1000
            }
        },
        "maxTeamSize": 4,
        "challenges": [
            {
                "id": "test1",
                "questionTitle": "Partner Organization",
                "description": "Who are the Partner organization of Praxis?",
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
                ],
                "scoring": {
                    "points": 100,
                    "timeDecay": {
                        "type": "none",
                        # "timeLimit": 0
                    }
                },
                "response": {
                    "type": "multiple_choice",
                    "choices": [
                        "A.J. O'Connor",
                        "NASA",
                        "Center for Creative Leadership",
                        "Pet Rock"
                    ],
                    "possibleAnswers": [0, 2]
                }
            },
            {
                "id": "test2",
                "questionTitle": "Approx of Employees at Praxis Engineering in North America",
                "description": "How many employees does Praxis Engineering have in North America?",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type your numeric answer here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Look at our about page"
                    },
                ],
                "scoring": {
                    "points": 100,
                    "timeDecay": {
                        "type": "none",
                        # "timeLimit": 0
                    }
                },
                "response": {
                    "type": "number_range",
                    "minAnswer": 200,
                    "maxAnswer": 250,
                    # TODO: needs a field called "possibleAnswers" which is a list  of all possible dates
                }
            },
            {
                "id": "test3",
                "questionTitle": "Praxis CEO",
                "description": "When did Dave Blanchard become the CEO of Praxis?",
                "imageURL": "https://aidmelvin.github.io/personal-website/praxis_cto.png",
                "placeholderText": "Type your numeric answer here:",
                "sequence": {
                    "num": 1,
                    "order": 1
                },
                "hints": [
                    {
                        "type": "string",
                        "penalty": 25,
                        "text": "Look at our about page"
                    },
                ],
                "scoring": {
                    "points": 100,
                    "timeDecay": {
                        "type": "none",
                        # "timeLimit": 0
                    }
                },
                "response": {
                    "type": "date_time",
                    "minAnswer": datetime(2011, 4, 1).isoformat(),
                    "maxAnswer": datetime(2011, 4, 30).isoformat(),
                    # TODO: needs a field called "possibleAnswers" which is a list  of all possible dates
                }
            },
           
        ],
        "teams": []
    }

    def do(self):
        hunt_ids = []

        for hunt_data in [self.hunt1_json, self.hunt2_json, self.hunt3_json, self.hunt4_json, self.hunt5_json]:
            response = requests.post(
                'http://localhost:8001/hunts/create_hunt', headers=self.headers, json=hunt_data)
            hunt_ids.append(json.loads((response.__dict__.get('_content')).decode('utf-8')).get('inserted_hunt_id'))
        
        return hunt_ids
