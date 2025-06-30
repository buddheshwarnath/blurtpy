import os
import pytest
from blurt.core.voice_config import VoiceConfig
from blurt.constants import DEFAULT_CONFIG, ENV_CONFIG_KEY


def test_voice_config_priority_user_over_env(monkeypatch):
    monkeypatch.setenv(ENV_CONFIG_KEY, '{"rate": 100, "volume": 0.2, "voice": "env_voice"}')
    config = VoiceConfig({"rate": 300, "volume": 0.5, "voice": "user_voice"})
    result = config.as_dict()
    assert result["rate"] == 300
    assert result["volume"] == 0.5
    assert result["voice"] == "user_voice"


def test_voice_config_env_used_if_no_user(monkeypatch):
    monkeypatch.setenv(ENV_CONFIG_KEY, '{"rate": 150, "volume": 0.6, "voice": "env_voice"}')
    config = VoiceConfig()
    result = config.as_dict()
    assert result["rate"] == 150
    assert result["volume"] == 0.6
    assert result["voice"] == "env_voice"


def test_voice_config_defaults(monkeypatch):
    monkeypatch.delenv(ENV_CONFIG_KEY, raising=False)
    config = VoiceConfig()
    assert config.as_dict() == DEFAULT_CONFIG


def test_voice_config_invalid_env(monkeypatch, capsys):
    monkeypatch.setenv(ENV_CONFIG_KEY, '{"rate": 100, volume}')  # Invalid JSON
    config = VoiceConfig()
    out = capsys.readouterr().out
    assert "[blurtpy] Warning: BLURT_CONFIG is not valid JSON." in out
