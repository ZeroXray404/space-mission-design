from . import interface, player

"""
Game engine
"""

def start_mission():
    interface.clear_screen()
    print("=== NEW MISSION ===")

    player_name = input("What's your name? ")
    player_one = player.Player(player_name)

    select_role(player_one)

    print(f"\nWelcome, {player_one.name}!")
    print(f"Your role: {player_one.role}")
    input("\nPress ENTER to continue...")


def select_role(player_one):
    while True:
        interface.clear_screen()

        print("=== SELECT ROLE ===")
        print("1. Mission Commander")
        print("2. Systems Engineer")
        print("3. Flight Operator")

        choice = input("Select a role: ")

        if choice == "1":
            player_one.set_role("Mission Commander")
            break

        elif choice == "2":
            player_one.set_role("Systems Engineer")
            break

        elif choice == "3":
            player_one.set_role("Flight Operator")
            break

        else:
            print("\nInvalid role. Please try again.")
            input("Press ENTER to continue...")
