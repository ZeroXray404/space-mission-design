"""
Player classes
"""


# Main player class
class Player:
    def __init__(self, name):
        self.name = name
        # Variable to be updated upon players choice of role
        self.role = None

    # Function to update players role
    def set_role(self, role):
        self.role = role
