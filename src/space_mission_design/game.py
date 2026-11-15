from . import interface, mission, player

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

    ongoing_mission = mission.OngoingMission()
    phases = [
        mission.design_phase
    ]

    while ongoing_mission.phase < len(phases):
        current_phase = phases[ongoing_mission.phase]

        play_phase(ongoing_mission, current_phase)
        ongoing_mission.phase += 1

        input("Press ENTER to return to main menu...")


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


def play_phase(ongoing_mission, current_phase):
    running = True

    while running:
        interface.clear_screen()
        print(f"=== {current_phase.title.upper()} ===")
        print(f"\nBudget: {ongoing_mission.budget}")
        print(f"Battery: {ongoing_mission.battery}%")

        print("\n1. Read mission briefing")
        print("2. Make decision")
        print("3. Review decisions")
        print("4. Continue to next phase")
        print("q. Quit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            print(f"\n{current_phase.description}")
            input("\nPress ENTER to continue...")

        elif choice == "2":
            print("Choose an alternative")
            input("\nPress ENTER to continue...")

        elif choice == "3":
            print("Current decision")
            input("\nPress ENTER to continue...")

        elif choice == "4":
            print("Next phase")
            input("\nPress ENTER to continue...")

        elif choice == "q":
            print("\nLeaving mission...\n")
            running = False

        else:
            print("\nInvalid option.")
            input("Press ENTER to continue...")