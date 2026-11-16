"""
Mission classes and functions
"""

import random


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


# Function for calculating budget overruns
def budget_overrun(
    list_cost: float, overrun_factor: float, overrun_likelihood: float
) -> float:
    likelihood_draw = random.random()  # Draws a float between 0 and 1
    if overrun_likelihood >= likelihood_draw:  # Project has run over budget
        overrun_draw = 1 + random.uniform(0, overrun_factor)
        actual_budget = round((list_cost * overrun_draw), 2)
    else:
        actual_budget = list_cost
    return actual_budget


# Mocked data. Later: read from JSON or yml
# Power is in watts, weight in kilograms, and reliability is a probability.
design_phase = MissionPhase(
    "Satellite Design",
    "Choose your CubeSat power system.",
    [
        {
            "name": "Basic solar panels",
            "description": (
                "Body-mounted solar panels. "
                "Simple construction with no deployment mechanism. "
                "Limited power generation."
            ),
            "budget": 10,
            "power": 10,
            "weight": 0.7,
            "reliability": 0.98,
        },
        {
            "name": "Advanced solar panels",
            "description": (
                "Deployable solar arrays with increased "
                "power generation. Requires a deployment "
                "mechanism that introduces additional risk."
            ),
            "budget": 30,
            "power": 25,
            "weight": 0.5,
            "reliability": 0.93,
        },
    ],
)

# Descriptions: NASA CubeSat 101, October 2017, sections 3.1, 3.4 and 3.5.
# Vehicle names and numeric values are fictional game data.
model_phase = MissionPhase(
    "Select Launch Vehicle",
    "Which Launch Vehicle should be used?",
    [
        {
            "name": "Astra V",
            "description": (
                "Fly as a secondary payload on a NASA-procured launch when "
                "the primary mission allows it. Your team submits documents "
                "through the mission integrator for NASA LSP approval and "
                "presents a readiness review."
            ),
            "mission model": "NASA-Procured",
            "budget": 30,
            # "fuel consumption": ,
            # "weight": ,
            "loading time": 6,
            "max overrun": 0.1,
            "overrun likelihood": 0.6,
        },
        {
            "name": "Stella X",
            "description": (
                "Share a NASA-procured launch as a secondary payload. "
                "The mission integrator coordinates documentation, interface "
                "verification and dispenser integration. Your team provides "
                "regular status updates and presents a readiness review."
            ),
            "mission model": "NASA-Procured",
            "budget": 25,
            # "fuel consumption": ,
            # "weight": ,
            "loading time": 8,
            "max overrun": 0.32,
            "overrun likelihood": 0.5,
        },
        {
            "name": "Aurora II",
            "description": (
                "Purchase a launch opportunity through a third-party broker. "
                "Launch requirements come from the launch vehicle provider "
                "through the broker, which acts as or appoints the mission "
                "integrator."
            ),
            "mission model": "Third-party brooker",
            "budget": 50,
            # "fuel consumption": ,
            # "weight": ,
            "loading time": 5,
            "max overrun": 0.15,
            "overrun likelihood": 0.1,
        },
        {
            "name": "Luna B Series III",
            "description": (
                "Arrange a commercial launch through a third-party broker. "
                "The assigned mission integrator works with your team and "
                "the launch vehicle provider to define the dispenser interface "
                "and schedule document and hardware deliveries."
            ),
            "mission model": "Third-party brooker",
            "budget": 22.6,
            # "fuel consumption": ,
            # "weight": ,
            "loading time": 11.5,
            "max overrun": 0.7,
            "overrun likelihood": 0.8,
        },
        {
            "name": "Atlas 38",
            "description": (
                "Travel to the ISS inside a pressurized cargo vessel, then "
                "deploy from the station. Your CubeSat is installed in its "
                "dispenser on the ground and must meet ISS-specific interface "
                "and flight safety requirements."
            ),
            "mission model": "ISS-mission",
            "budget": 30,
            # "fuel consumption": ,
            # "weight": ,
            "loading time": 8,
            "max overrun": 0.05,
            "overrun likelihood": 0.65,
        },
    ],
)


class Mission:
    def __init__(self, mission_file):
        pass

    def read_mission_file(self, mission_file):
        pass
