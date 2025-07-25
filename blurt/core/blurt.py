"""
core/blurt.py - Defines the Blurt class that provides voice actions using platform-specific drivers.
This is the main entry point for all class-based usage.
"""

import platform
from typing import Optional, Dict, List

from blurt.core.voice_config import VoiceConfig
from blurt.drivers.driver_factory import DriverFactory
from blurt.constants import DEFAULT_SOUND_FILE


class Blurt:
    """
    Blurt is a cross-platform voice utility class that lets you speak messages, beep, or play sounds.
    It supports macOS, Linux, and Windows, and automatically chooses the correct driver.
    """

    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize Blurt with optional config (rate, volume, voice, etc.)
        Priority: user config > env config > default config
        """
        self.config = VoiceConfig(config).as_dict()
        self.driver = DriverFactory.get_driver(self.config)

    def say(self, message: str):
        """Speak a message aloud."""
        self.driver.say(message)

    def beep(self):
        """Play a beep sound."""
        self.driver.beep()

    def play_sound(self, path: Optional[str] = None):
        """
        Play a sound file. Defaults to alert.mp3.
        """
        if not path:
            path = DEFAULT_SOUND_FILE
        self.driver.play_sound(path)

    def list_voices(self) -> List[str]:
        """Return available voices on the system."""
        return self.driver.list_voices()

    def set_rate(self, rate: int):
        """Set the speaking rate."""
        self.driver.set_rate(rate)

    def set_volume(self, volume: float):
        """Set the speaking volume."""
        self.driver.set_volume(volume)

    def set_voice(self, voice: str):
        """Set the system voice."""
        self.driver.set_voice(voice)
