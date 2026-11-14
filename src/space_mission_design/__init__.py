from . import game, interface

"""
Game main menu
"""

def main() -> None:
    interface.startup()
    running = True

    while running:
        interface.clear_screen()
        choice = interface.main_menu()

        if choice == "1":
            game.start_mission()

        elif choice == "2":
            interface.about_cubesats()

        elif choice == "3":
            interface.mission_handbook()

        elif choice == "4":
            print("\nExiting mission simulator...\n")
            running = False

        else:
            print("\nInvalid option. Please try again.")
            input("Press ENTER to continue...")