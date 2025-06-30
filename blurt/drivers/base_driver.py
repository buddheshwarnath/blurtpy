"""
base_driver.py - Abstract base class for all OS-specific drivers (macOS, Linux, Windows).
Defines a consistent interface that all driver implementations must follow.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from blurt.constants import BEEP_SOUND_FILE


class BaseDriver(ABC):
    """
    Abstract base driver that defines the common interface for all platform-specific drivers.
    All child drivers (macOS, Linux, Windows) must implement these methods.
    """

    def __init__(
        self, rate: int = 200, volume: float = 1.0, voice: Optional[str] = None, 
        pitch: Optional[int] = None, language: Optional[str] = None
    ):
        """
        Initialize the driver with common configuration.
        """
        self.rate = rate
        self.volume = volume
        self.voice = voice
        self.pitch = pitch
        self.language = language

    @abstractmethod
    def say(self, message: str):
        """
        Speak the given message aloud.
        """
        pass

    def beep(self):
        """
        Produce a short beep sound.
        """
        self.play_sound(BEEP_SOUND_FILE)

    @abstractmethod
    def play_sound(self, path: Optional[str] = None):
        """
        Play a sound file at the given path.
        """
        pass

    @abstractmethod
    def list_voices(self) -> List[str]:
        """
        List all available voices on the system (if supported).
        """
        pass

    def set_rate(self, rate: int):
        """Set the speaking rate."""
        self.rate = rate

    def set_volume(self, volume: float):
        """Set the speaking volume."""
        self.volume = volume

    def set_voice(self, voice: str):
        """Set the system voice to use."""
        self.voice = voice
