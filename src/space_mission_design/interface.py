"""
Interface engine
"""

import shutil
import textwrap


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


def display_description(description, indent=""):
    # Include indentation in the limit of half the current terminal width.
    width = max(1, shutil.get_terminal_size(fallback=(80, 24)).columns // 2)
    indent = indent[: width - 1]
    print(
        textwrap.fill(
            description,
            width=width,
            initial_indent=indent,
            subsequent_indent=indent,
        )
    )


def display_choices(current_phase):
    # Show each choice with its description and available technical data
    print(f"=== {current_phase.title.upper()} ===\n")
    display_description(current_phase.description)
    print()

    for index, choice in enumerate(current_phase.choices, start=1):
        print(f"{index}. {choice['name']}")

        description = choice.get("description")
        if description:
            display_description(description, indent="   ")

        if "power" in choice:
            print(f"   Power: {choice['power']} W")

        if "weight" in choice:
            print(f"   Weight: {choice['weight']} kg")

        if "reliability" in choice:
            print(f"   Reliability: {choice['reliability']:.0%}")

        if "mission model" in choice:
            print(f"   Mission model: {choice['mission model']}")

        if "loading time" in choice:
            print(f"   Loading time: {choice['loading time']}")

        if "max overrun" in choice:
            print(f"   Max overrun: {choice['max overrun']}")

        if "overrun likelihood" in choice:
            print(f"   Overrun likelihood: {choice['overrun likelihood']:.0%}")

        print(f"   Cost: {choice['budget']} credits")
        print()


def about_cubesats():
    clear_screen()
    print("About CubeStats")
    input("\nPress ENTER to return...")


def mission_handbook():
    clear_screen()
    print("Mission handbook")
    input("\nPress ENTER to return...")
