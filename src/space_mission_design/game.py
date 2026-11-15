from . import interface, mission, player  # , score

"""
Game engine
"""


# Mission
def start_mission():
    interface.clear_screen()
    print("=== NEW MISSION ===\n")

    player_name = input("What's your name? ")
    player_one = player.Player(player_name)

    select_role(player_one)

    print(f"\nWelcome, {player_one.name}!")
    print(f"Your role: {player_one.role}")
    input("\nPress ENTER to continue...")

    ongoing_mission = mission.OngoingMission()
    # mission_score = score.Score()
    phases = [mission.design_phase, mission.model_phase]

    while ongoing_mission.phase < len(phases):
        current_phase = phases[ongoing_mission.phase]
        completed = play_phase(ongoing_mission, current_phase)

        if not completed:
            print("\nMission aborted!")
            input("Press ENTER to return to main menu...")
            return

        ongoing_mission.phase += 1

        # Check current phase status
        if ongoing_mission.phase < len(phases):
            print("\nPhase completed!")
            input("press ENTER to continue to next phase")

    print(
        f"\nCongratulations {player_one.role} {player_one.name}! The mission was a success!"
    )
    input("Press ENTER to return to main menu...")


# Handle player role input & updates Player
def select_role(player_one):
    while True:
        interface.clear_screen()

        print("=== SELECT ROLE ===\n")
        print("1. Mission Commander")
        print("2. Systems Engineer")
        print("3. Flight Operator\n")

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


# Handle player decision & updates OngoingMission
def make_decision(ongoing_mission, current_phase):
    interface.clear_screen()
    print(f"=== {current_phase.title.upper()} ===\n")

    for index, choice in enumerate(current_phase.choices, start=1):
        print(f"{index}. {choice['name']}")

    selected = input("\nSelect option: ")

    # Handle invalid input
    if not selected.isdigit():
        print("\nInvalid input.")
        input("\nPress ENTER to continue...")
        return

    index = int(selected) - 1

    if index < 0 or index >= len(current_phase.choices):
        print("\nInvalid input.")
        input("\nPress ENTER to continue...")
        return

    # Check budget
    choice = current_phase.choices[index]
    new_budget = ongoing_mission.budget + choice["budget"]

    if new_budget < 0:
        print("Insufficient budget.")
        input("Press ENTER to continue...")
        return

    # Save decision
    ongoing_mission.budget = new_budget
    ongoing_mission.decisions.append(
        {
            "phase": current_phase.title,
            "choice": choice["name"],
        }
    )
    print(f"\nSelected: {choice['name']}")
    print(f"Budget remaining: {ongoing_mission.budget} credits")
    input("\nPress ENTER to continue...")


def check_decision(ongoing_mission, current_phase):
    interface.clear_screen()
    print(f"=== {current_phase.title.upper()} ===\n")
    print("Your CubeSat is equipped with: ")
    for index, decision in enumerate(ongoing_mission.decisions, start=1):
        if decision == "":
            print("No equipment mounted")
        else:
            print(f"{index}. {decision['choice']}")

    input("\nPress ENTER to continue...")


def phase_completed(ongoing_mission, current_phase):
    for decision in ongoing_mission.decisions:
        if decision["phase"] == current_phase.title:
            return True
    return False


# Handle in-game phase menu
def play_phase(ongoing_mission, current_phase):
    running = True

    while running:
        interface.clear_screen()
        print(f"=== {current_phase.title.upper()} ===")
        print(f"\nBudget: {ongoing_mission.budget} credits")
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
            if phase_completed(ongoing_mission, current_phase):
                print("\nYou have already made a decision in this phase.")
                input("Press ENTER to continue...")
            else:
                make_decision(ongoing_mission, current_phase)

        elif choice == "3":
            check_decision(ongoing_mission, current_phase)

        elif choice == "4":
            if phase_completed(ongoing_mission, current_phase):
                return True
            print("\nYou must make a decision before continuing\n")
            input("Press ENTER to continue...")

        elif choice == "q":
            print("\nLeaving mission...")
            running = False
            return False

        else:
            print("\nInvalid option.")
            input("Press ENTER to continue...")
