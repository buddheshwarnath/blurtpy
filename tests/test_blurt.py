import os
import pytest
from blurt import say, beep, play_sound, list_voices, Blurt
from blurt.core.voice_config import VoiceConfig

def test_say_runs_without_crash():
    say("This is a test message.")

def test_beep_does_not_crash():
    beep()

def test_play_sound_default():
    play_sound()  # Uses DEFAULT_SOUND_FILE

def test_list_voices_returns_list():
    voices = list_voices()
    assert isinstance(voices, list)

def test_blurt_class_say():
    blurt = Blurt()
    blurt.say("Blurt class says hi!")

def test_blurt_env_config(monkeypatch):
    monkeypatch.setenv("BLURT_CONFIG", '{"rate": 190, "volume": 0.7}')
    blurt = Blurt()
    assert isinstance(blurt, Blurt)
    blurt.say("Environment config test.")

def test_voice_config_priority(monkeypatch):
    monkeypatch.setenv("BLURT_CONFIG", '{"rate": 190, "volume": 0.7}')
    cfg = VoiceConfig({"rate": 210})
    assert cfg.get("rate") == 210
    assert cfg.get("volume") == 0.7

def test_voice_config_repr():
    cfg = VoiceConfig()
    assert "VoiceConfig" in repr(cfg)
