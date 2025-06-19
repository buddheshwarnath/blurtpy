'''
blurt/__init__.py - core package init
'''

import platform
import os
import subprocess
import pyttsx3
from functools import wraps
import inspect
from contextlib import contextmanager
from playsound import playsound

# Linux-only install-time warning
if platform.system() == "Linux":
    if subprocess.run(["which", "espeak"], capture_output=True).returncode != 0 and \
       subprocess.run(["which", "spd-say"], capture_output=True).returncode != 0:
        print("[blurt] Voice output is unavailable. Install with:\nsudo apt install espeak")

__all__ = ['say', 'notify_when_done', 'speak', 'beep', 'play_sound']

BLURT_MUTE = os.getenv("BLURT_MUTE", "false").lower() in ["1", "true", "yes"]

def say(message: str):
    if BLURT_MUTE:
        print(f"[🔇 muted] {message}")
        return
    if not message:
        print("[blurt] No message to speak.")
        return
    
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(["say", message])
        elif system == "Linux":
            if subprocess.run(["which", "espeak"], capture_output=True).returncode == 0:
                subprocess.run(["espeak", message])
            elif subprocess.run(["which", "spd-say"], capture_output=True).returncode == 0:
                subprocess.run(["spd-say", message])
            else:
                print(f"[🔇 fallback] {message}")
                print("[blurt] Voice not available. To enable sound on Linux:\nsudo apt install espeak")
        elif system == "Windows":
            engine = pyttsx3.init()
            engine.say(message)
            engine.runAndWait()
        else:
            print(f"[Unknown OS] {message}")
    except Exception as e:
        print(f"[Error Speaking] {message} - {e}")

def notify_when_done(message: str = "Task completed"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            say(message)
            return result
        return wrapper
    return decorator

@contextmanager
def speak(start: str = "Started", done: str = "Completed"):
    say(start)
    try:
        yield
    finally:
        say(done)

def beep():
    try:
        system = platform.system()
        if system == "Windows":
            import winsound
            winsound.Beep(1000, 200)
        elif system == "Darwin":
            subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])
        elif system == "Linux":
            print("\a", end='', flush=True)
    except Exception as e:
        print(f"[blurt] Beep failed: {e}")

def play_sound(path: str = None):
    try:
        if not path:
            # Use default bundled sound
            path = os.path.join(os.path.dirname(__file__), "assets", "alert.mp3")
        
        path = os.path.abspath(path)
        playsound(path)
    except Exception as e:
        print(f"[blurt] Sound failed: {e}")
