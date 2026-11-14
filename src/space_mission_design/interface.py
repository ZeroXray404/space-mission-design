"""
Interface engine
"""

# Clear screen and 
def clear_screen():
    print(chr(27) + "[2J" + chr(27) + "[;H", end="")


# Startup of simulation
def startup():
    print("Initializing mission simulator...")
    input("Press ENTER to continue...")


# Main menu
def main_menu():
    print("\n=== CUBESAT 101 ===")
    print("1. Start new mission")
    print("2. About CubeSats")
    print("3. Mission handbook")
    print("4. Exit")

    return input("\nSelect an option: ")


def about_cubesats():
    print("About CubeStats")


def mission_handbook():
    print("Mission handbook")