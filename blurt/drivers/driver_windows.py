"""
driver_windows.py - Windows-specific implementation of the BaseDriver interface.
Uses pyttsx3 for TTS and winsound for sound playback and beeping.
"""

from typing import List, Optional
from blurt.constants import DEFAULT_SOUND_FILE
from blurt.drivers.base_driver import BaseDriver


class WindowsDriver(BaseDriver):
    """
    Windows-specific driver using pyttsx3 for text-to-speech and winsound for audio.
    """

    def __init__(self, rate=200, volume=1.0, voice=None, pitch=None, language=None):
        import pyttsx3  # Safe, as only Windows will reach here
        super().__init__(rate=rate, volume=volume, voice=voice, pitch=pitch, language=language)
        try:
            self.engine = pyttsx3.init()
            self._apply_config()
        except Exception as e:
            print(f"[blurt] Failed to initialize pyttsx3: {e}")
            self.engine = None

    def _apply_config(self):
        if not self.engine:
            return
        try:
            if self.rate:
                self.engine.setProperty("rate", self.rate)
            if self.volume is not None:
                self.engine.setProperty("volume", self.volume)
            if self.voice:
                voices = self.engine.getProperty("voices")
                matched = [v for v in voices if self.voice in v.id or self.voice in v.name]
                if matched:
                    self.engine.setProperty("voice", matched[0].id)
        except Exception as e:
            print(f"[blurt] Failed to apply voice config: {e}")

    def say(self, message: str):
        if not message:
            print("[blurt] No message to speak.")
            return
        try:
            self.engine.say(message)
            self.engine.runAndWait()
        except Exception as e:
            print(f"[blurt] Windows say failed: {e}")

    def play_sound(self, path: Optional[str] = None):
        path = path or DEFAULT_SOUND_FILE
        try:
            import winsound  # Moved inside
            winsound.PlaySound(path, winsound.SND_FILENAME)
        except Exception as e:
            print(f"[blurt] Sound failed: {e}")

    def list_voices(self) -> List[str]:
        try:
            voices = self.engine.getProperty("voices")
            return [f"{v.id} ({v.name})" for v in voices]
        except Exception as e:
            print(f"[blurt] Failed to list voices: {e}")
            return []
