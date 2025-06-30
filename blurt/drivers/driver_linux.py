"""
driver_linux.py - Linux-specific implementation of the BaseDriver interface.
Supports speech via `espeak` or `spd-say`, and sound playback via `aplay`.
"""

import subprocess
from shutil import which
from typing import List, Optional
from .base_driver import BaseDriver
from blurt.constants import DEFAULT_SOUND_FILE


class LinuxDriver(BaseDriver):
    """
    Linux-specific driver for speech and sound functionalities.
    Prefers `espeak` if available, falls back to `spd-say` or terminal bell.
    """

    def __init__(self, rate=200, volume=1.0, voice=None, pitch=None, language=None):
        super().__init__(rate=rate, volume=volume, voice=voice, pitch=pitch, language=language)
        self.has_espeak = which("espeak") is not None
        self.has_spdsay = which("spd-say") is not None
        self.has_aplay = which("aplay") is not None

        if not self.has_espeak and not self.has_spdsay:
            print("[blurt] Warning: No supported TTS engine found. Install with: sudo apt install espeak")

    def say(self, message: str):
        """
        Speak a message using espeak or spd-say.
        Applies voice, rate, and pitch if supported by the backend.
        """
        if not message:
            print("[blurt] No message to speak.")
            return

        try:
            if self.has_espeak:
                cmd = ["espeak", message]
                if self.rate:
                    cmd += ["-s", str(self.rate)]
                if self.voice:
                    cmd += ["-v", self.voice]
                if self.pitch:
                    cmd += ["-p", str(self.pitch)]
                subprocess.run(cmd, check=True)

            elif self.has_spdsay:
                subprocess.run(["spd-say", message], check=True)
            else:
                print(f"[🔇 fallback] {message}")
        except Exception as e:
            print(f"[blurt] Linux say failed: {e}")

    def play_sound(self, path: Optional[str] = None):
        """
        Play an audio file using `aplay`.
        If no path is provided, uses the default alert sound.
        """
        path = path or DEFAULT_SOUND_FILE

        try:
            if self.has_aplay:
                subprocess.run(["aplay", path], check=True)
            else:
                print(f"[blurt] aplay not found. Install with: sudo apt install alsa-utils")
        except Exception as e:
            print(f"[blurt] Sound playback failed: {e}")

    def list_voices(self) -> List[str]:
        """
        Returns voice list supported by espeak.
        """
        voices = []
        try:
            if self.has_espeak:
                result = subprocess.run(["espeak", "--voices"], capture_output=True, text=True)
                lines = result.stdout.splitlines()[1:]  # Skip header
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 4:
                        voices.append(parts[3])  # Voice name
            return voices
        except Exception as e:
            print(f"[blurt] Failed to list voices: {e}")
            return []
