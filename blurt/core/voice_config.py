"""
voice_config.py - Handles voice-related configuration loading and validation.
"""

import json
import os
from typing import Optional, Dict, Any

from blurt.constants import DEFAULT_CONFIG, CONFIG_KEYS, ENV_CONFIG_KEY


class VoiceConfig:
    """
    VoiceConfig handles all speech-related settings such as rate, volume,
    language, voice, and pitch. Priority order:
    1. User-passed config
    2. Environment config (BLURT_CONFIG as JSON)
    3. Default config
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initializes a VoiceConfig instance with merged configuration.

        :param config: Optional dictionary with keys from CONFIG_KEYS.
        """
        self._config = DEFAULT_CONFIG.copy()

        # Medium priority: environment config
        env_config_str = os.getenv(ENV_CONFIG_KEY)
        if env_config_str:
            try:
                env_config = json.loads(env_config_str)
                if isinstance(env_config, dict):
                    self._apply_config(env_config)
            except json.JSONDecodeError:
                print(f"[blurtpy] Warning: {ENV_CONFIG_KEY} is not valid JSON.")

        # High priority: user-passed config
        if config:
            self._apply_config(config)

    def _apply_config(self, config: Dict[str, Any]):
        """Applies valid config keys to internal config."""
        for key in CONFIG_KEYS:
            if key in config:
                self._config[key] = config[key]

    def get(self, key: str) -> Any:
        """Returns the config value for the given key."""
        return self._config.get(key)

    def as_dict(self) -> Dict[str, Any]:
        """Returns the entire config as a dictionary."""
        return self._config.copy()

    def __repr__(self):
        return f"<VoiceConfig {self._config}>"

    @staticmethod
    def from_dict(config: Dict[str, Any]) -> "VoiceConfig":
        """
        Creates a VoiceConfig instance from a plain config dictionary.
        """
        return VoiceConfig(config)
