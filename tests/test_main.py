import sys
import pytest
from blurt.__main__ import main

def test_main_say(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["blurt", "say", "Test from CLI"])
    main()
    # Output is spoken, but we can check for no crash

def test_main_beep(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["blurt", "beep"])
    main()
    # Output is a beep, check for no crash

def test_main_sound(monkeypatch, capsys):
    from blurt.constants import BEEP_SOUND_FILE
    monkeypatch.setattr(sys, "argv", ["blurt", "sound", BEEP_SOUND_FILE])
    main()
    # Output is a sound, check for no crash

def test_main_list_voices(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["blurt", "list-voices"])
    main()
    out = capsys.readouterr().out
    assert "Available voices:" in out or "No voices found" in out

def test_main_help(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["blurt"])
    main()
    out = capsys.readouterr().out
    assert "usage:" in out or "blurt commands" in out 