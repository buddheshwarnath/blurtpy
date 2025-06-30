"""
constants.py - Centralized constants for blurtpy package.
"""

import os
from pathlib import Path

# Get the directory where this constants file is located
PACKAGE_DIR = Path(__file__).parent
ASSETS_DIR = PACKAGE_DIR / "assets"

# Default config values
DEFAULT_RATE = 200           # Words per minute
DEFAULT_VOLUME = 1.0         # Max volume
DEFAULT_LANGUAGE = "en"      # Language code
DEFAULT_VOICE = None         # Will use system default voice if not set
DEFAULT_PITCH = None         # Optional pitch control


# Consolidated default config dict
DEFAULT_CONFIG = {
    "rate": DEFAULT_RATE,
    "volume": DEFAULT_VOLUME,
    "language": DEFAULT_LANGUAGE,
    "voice": DEFAULT_VOICE,
    "pitch": DEFAULT_PITCH,
}

# Supported config keys
CONFIG_KEYS = ["rate", "volume", "language", "voice", "pitch"]

# Environment variable to pick up config
ENV_CONFIG_KEY = "BLURT_CONFIG"

# Other constants
DEFAULT_START_MESSAGE = "Started"
DEFAULT_END_MESSAGE = "Completed"
DEFAULT_SOUND_FILE = str(ASSETS_DIR / "alert.mp3")
BEEP_SOUND_FILE = str(ASSETS_DIR / "beep.mp3")
