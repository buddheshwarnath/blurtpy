"""
global_blurt.py - Singleton Blurt instance used for all global functions and decorators.
"""

import os
import json
from blurt.core.blurt import Blurt
from blurt.constants import ENV_CONFIG_KEY


def _load_config_from_env() -> dict:
    """
    Load user-defined config from environment variable BLURT_CONFIG.
    Must be a valid JSON string.
    """
    config_str = os.getenv(ENV_CONFIG_KEY)
    if config_str:
        try:
            return json.loads(config_str)
        except json.JSONDecodeError:
            print("[blurtpy] Invalid BLURT_CONFIG. Must be valid JSON.")
    return {}


# Initialize global Blurt object with environment config (if present)
global_blurt = Blurt(config=_load_config_from_env())
