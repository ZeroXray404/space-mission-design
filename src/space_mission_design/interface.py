"""
Interface engine of game
"""

from . import player


# Startup of simulation
def startup() -> object:
    print("Initializing mission simulator...")
    player_name = input("What's your name? ")
    player_one = player.Player(player_name)
    return player_one
