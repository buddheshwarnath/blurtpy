"""
core/global_api.py - Global API functions for quick usage without needing to create a Blurt instance.
This is the recommended entry point for scripting and casual use.
"""

from typing import Optional, List
from blurt.core.blurt import Blurt
from blurt.constants import DEFAULT_SOUND_FILE

# Create global Blurt instance using env/default config
_global_blurt = Blurt()

def say(message: str):
    """
    Speak the given message aloud using the global Blurt instance.
    """
    _global_blurt.say(message)

def beep():
    """
    Play a simple beep sound using the global Blurt instance.
    """
    _global_blurt.beep()

def play_sound(path: Optional[str] = None):
    """
    Play a sound file. If no path is provided, play the default alert sound.
    """
    if not path:
        path = DEFAULT_SOUND_FILE
    _global_blurt.play_sound(path)

def list_voices() -> List[str]:
    """
    Return a list of available voices supported on this system.
    """
    return _global_blurt.list_voices()

def set_rate(rate: int):
    """
    Set the global speaking rate.
    """
    _global_blurt.set_rate(rate)

def set_volume(volume: float):
    """
    Set the global speaking volume.
    """
    _global_blurt.set_volume(volume)

def set_voice(voice: str):
    """
    Set the global voice to use for speaking.
    """
    _global_blurt.set_voice(voice)
