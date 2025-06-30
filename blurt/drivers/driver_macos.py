"""
driver_macos.py - macOS-specific implementation of the BaseDriver interface.
Uses built-in macOS commands like 'say' and 'afplay' for speech and sound playback.
"""

import subprocess
from typing import List, Optional
from .base_driver import BaseDriver
from blurt.constants import DEFAULT_SOUND_FILE


class MacOSDriver(BaseDriver):
    """
    macOS-specific voice and sound driver.
    Relies on built-in tools: `say` for text-to-speech and `afplay` for playing audio files.
    """

    def __init__(self, rate=200, volume=1.0, voice=None, pitch=None, language=None):
        super().__init__(rate=rate, volume=volume, voice=voice, pitch=pitch, language=language)

    def say(self, message: str):
        """
        Speak the given message using the `say` command.

        Supports optional voice and rate adjustments.
        Volume control is not supported natively by `say`.
        """
        if not message:
            print("[blurt] No message to speak.")
            return

        command = ["say"]
        if self.voice:
            command += ["-v", self.voice]
        if self.rate:
            command += ["-r", str(self.rate)]

        command.append(message)

        try:
            subprocess.run(command, check=True)
        except Exception as e:
            print(f"[blurt] macOS say failed: {e}")

    def play_sound(self, path: Optional[str] = None):
        """
        Play an audio file using `afplay`.
        If no path is provided, uses the default alert sound from constants.
        """
        path = path or DEFAULT_SOUND_FILE
        print(path)
        try:
            subprocess.run(["afplay", path], check=True)
        except Exception as e:
            print(f"[blurt] Sound playback failed: {e}")

    def list_voices(self) -> List[str]:
        """
        List all available voices using `say -v ?`.
        Returns a list of voice names.
        """
        try:
            result = subprocess.run(["say", "-v", "?"], capture_output=True, text=True)
            voices = []
            for line in result.stdout.splitlines():
                parts = line.split()
                if parts:
                    voices.append(parts[0])
            return voices
        except Exception as e:
            print(f"[blurt] Failed to list voices: {e}")
            return []
