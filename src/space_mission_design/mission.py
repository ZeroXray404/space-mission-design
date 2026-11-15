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
        },
        {
            "name": "Advanced solar panels",
            "budget": -30,
            "power": 25,
        },
    ],
)

class Mission:
    def __init__(self, mission_file):
        pass

    def read_mission_file(self, mission_file):
        pass

