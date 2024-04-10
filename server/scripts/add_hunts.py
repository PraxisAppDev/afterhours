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
                        "General Dynamics Corporation"
                        "General Dynamics Information Technology"
                    ],
                    "caseSensitive": False
                }
            },
            {
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
                    "type": "numeric_text_field",
                    "possibleAnswers": [
                        2002
                    ],
                    "caseSensitive": False
                }
            },
            {
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
                    "type": "string_list_text_field",
                    "possibleAnswers": [
                        "Customer Success"
                        "Employee Success",
                        "Technical Excellence",
                        "Fiscal Responsibility",
                        "Social Awareness"
                    ],
                    "caseSensitive": False
                }
            },
            {
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
                    "type": "numeric_text_field",
                    "possibleAnswers": [
                        350
                    ],
                    "caseSensitive": False
                }
            },
            {
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
                    "type": "list_text_field",
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
                    "caseSensitive": False
                }
            },
        ],
        "teams": []
    }

    hunt3_json = {
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
                    "type": "string_list_text_field",
                    "possibleAnswers": [
                        "NSA",
                        "CIA",
                        "DOD"
                    ],
                    "caseSensitive": False
                }
            },
            {
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
                    "type": "numeric_text_field",
                    "possibleAnswers": [
                        50
                    ],
                    "caseSensitive": False
                }
            },
            {
                "questionTitle": "Why Praxis",
                "description": "Name 3 benefits of Praxis",
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
                    "type": "string_list_text_field",
                    "possibleAnswers": [
                        "Let your voice be heard",
                        "Grow your geek",
                        "It's all about the balance",
                        "Less is more? Since when!",
                        "Whole self health"
                    ],
                    "caseSensitive": False
                }
            },
        ],
        "teams": []
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
        "teams": []
    }

    # change("goob@gmail.com", "silly silly", "bl@hbl@h101", "raaaa raaaa")
    def do(self):
        response = requests.post(
            'http://localhost:8001/hunts/create_hunt', headers=self.headers, json=self.json_data)
        return json.loads((response.__dict__.get('_content')).decode('utf-8')).get('inserted_hunt_id')
