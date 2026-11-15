"""
Mission class
"""


class OngoingMission:
    def __init__(self):
        self.phase = 0
        self.budget = 100
        self.battery = 100
        self.score = 0
        self.decisions = []


class MissionPhase:
    def __init__(self, title, description, choices):
        self.title = title
        self.description = description
        self.choices = choices


# Mocked data. Later: read from JSON or yml
design_phase = MissionPhase(
    "Satellite Design",
    "Choose your CubeSat power system.",
    [
        {
            "name": "Basic solar panels",
            "budget": -10,
            "power": 10,
            "weight": 7
        },
        {
            "name": "Advanced solar panels",
            "budget": -30,
            "power": 25,
            "weight": 5
        },
    ],
)

model_phase = MissionPhase(
    "Select Launch Vehicle",
    "Which Launch Vehicle should be used?",
    [
        {
            "name": "Astra V",
            "mission model": "NASA-Procured",
            "budget": -30,
            #"fuel consumption": ,
            #"weight": ,
            "loading time": 6,
            "max overrun": 1.1,
            "overrun likelihood": 0.6
        },
        {
            "name": "Stella X",
            "mission model": "NASA-Procured",
            "budget": -25,
            #"fuel consumption": ,
            #"weight": ,
            "loading time": 8,
            "max overrun": 1.32,
            "overrun likelihood": 0.5
        },
        {
            "name": "Aurora II",
            "mission model": "Third-party brooker" ,
            "budget": -50,
            #"fuel consumption": ,
            #"weight": ,
            "loading time": 5,
            "max overrun": 1.15,
            "overrun likelihood": 0.1
        },
        {
            "name": "Luna B Series III",
            "mission model": "Third-party brooker" ,
            "budget": -22.6,
            #"fuel consumption": ,
            #"weight": ,
            "loading time": 11.5,
            "max overrun": 1.7,
            "overrun likelihood": 0.8
        },
        {
            "name": "Atlas 38",
            "mission model": "ISS-mission",
            "budget": -30,
            #"fuel consumption": ,
            #"weight": ,
            "loading time": 8,
            "max overrun": 1.05,
            "overrun likelihood": 0.65
        }
    ]
)


class Mission:
    def __init__(self, mission_file):
        pass

    def read_mission_file(self, mission_file):
        pass
