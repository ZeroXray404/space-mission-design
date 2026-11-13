"""Smoke tests for the CLI entry point."""

from space_mission_design import main


def test_main_prints_starter_message(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from space-mission-design!\n"
