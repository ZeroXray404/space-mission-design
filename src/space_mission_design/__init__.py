from . import interface


def main() -> None:
    interface.startup()
    player_info = interface.startup()
    print("Hello from space-mission-design! 🚀")
    print(player_info.name)
    return 0
