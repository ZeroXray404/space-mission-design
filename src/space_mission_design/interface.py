"""
Interface engine of game
"""

from . import player

# Clear screen and 
def clear_screen():
    print(chr(27) + "[2J" + chr(27) + "[;H", end="")


# Main menu
def main_menu():
    print("\n=== CUBESAT 101 ===")
    print("1. Start new mission")
    print("2. About CubeSats")
    print("3. Mission handbook")
    print("4. Exit")

    return input("Select an option: ")


# Startup of simulation
def startup():
    print("Initializing mission simulator...")

    running = True

    while running:
        clear_screen()
        choice = main_menu()

        if choice == "1":
            print("Starting new mission...")

        elif choice == "2":
            print("About CubeSats...")

        elif choice == "3":
            print("Opening mission handbook...")

        elif choice == "4":
            print("Exiting mission simulator...")
            running = False

        else:
            print("Invalid option. Please try again.")
def startup() -> object:
    print("Initializing mission simulator...")
    player_name = input("What's your name? ")
    player_one = player.Player(player_name)
    return player_one
