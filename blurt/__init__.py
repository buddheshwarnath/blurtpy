"""
blurtpy - Cross-platform voice feedback library for Python.

This package provides:
- Global utility functions: say, beep, play_sound, list_voices
- Decorators: notify_when_done, announce_during
- Blurt class for custom configurations
"""

from .core.blurt import Blurt
from .core.global_api import say, beep, play_sound, list_voices
from .core.decorators import notify_when_done, announce_during

__all__ = [
    "say",
    "beep",
    "play_sound",
    "list_voices",
    "notify_when_done",
    "announce_during",
    "Blurt"
]
