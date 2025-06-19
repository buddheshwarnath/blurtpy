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

# Linux-only install-time warning
if platform.system() == "Linux":
    if subprocess.run(["which", "espeak"], capture_output=True).returncode != 0 and \
       subprocess.run(["which", "spd-say"], capture_output=True).returncode != 0:
        print("[blurt] Voice output is unavailable. Install with:\nsudo apt install espeak")
        
__all__ = ['say', 'notify_when_done']

BLURT_MUTE = os.getenv("BLURT_MUTE", "false").lower() in ["1", "true", "yes"]


def say(message: str, mute: bool = False):
    if BLURT_MUTE or mute:
        print(f"[🔇 muted] {message}")
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
def speak(start: str = "Started", done: str = "Completed", mute: bool = False):
    say(start, mute=mute)
    try:
        yield
    finally:
        say(done, mute=mute)
