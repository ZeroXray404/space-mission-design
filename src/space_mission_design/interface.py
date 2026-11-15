"""
Interface engine
"""


# Clear screen
def clear_screen():
    print(chr(27) + "[2J" + chr(27) + "[;H", end="")


# Startup of simulation
def startup():
    clear_screen()
    print("Initializing mission simulator...")
    input("Press ENTER to continue...")


# Main menu
def main_menu():
    print("=== CUBESAT 101 ===\n")
    print("1. Start new mission")
    print("2. About CubeSats")
    print("3. Mission handbook")
    print("q. Quit")

    return input("\nSelect an option: ")


def about_cubesats():
    clear_screen()
    print("About CubeStats")
    input("\nPress ENTER to return...")


def mission_handbook():
    clear_screen()
    print("Mission handbook")
    input("\nPress ENTER to return...")
