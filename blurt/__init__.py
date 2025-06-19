'''
blurt/__init__.py - core package init
'''

import platform
import os
import subprocess
from functools import wraps
import inspect
from contextlib import contextmanager

# Linux-only install-time warning
if platform.system() == "Linux":
    if subprocess.run(["which", "espeak"], capture_output=True).returncode != 0 and \
       subprocess.run(["which", "spd-say"], capture_output=True).returncode != 0:
        print("[blurt] Voice output is unavailable. Install with:\nsudo apt install espeak")

__all__ = ['say', 'notify_when_done', 'speak', 'beep', 'play_sound']

BLURT_MUTE = os.getenv("BLURT_MUTE", "false").lower() in ["1", "true", "yes"]

def say(message: str):
    """
    Speak a message aloud using system-specific TTS (Text-To-Speech) tools.

    On Linux, uses `espeak` or `spd-say`.
    On macOS, uses the built-in `say` command.
    On Windows, uses the `pyttsx3` library.

    If the BLURT_MUTE environment variable is set to true/1/yes,
    this function will print the message instead of speaking it.

    Args:
        message (str): The message string to speak aloud.

    Returns:
        None
    """
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
            try:
                import pyttsx3
                engine = pyttsx3.init()
                engine.say(message)
                engine.runAndWait()
            except ImportError:
                print("[blurt] pyttsx3 not installed. Run: pip install pyttsx3")
        else:
            print(f"[Unknown OS] {message}")
    except Exception as e:
        print(f"[Error Speaking] {message} - {e}")

def notify_when_done(message: str = "Task completed"):
    """
    A decorator that announces a message via speech after the decorated function completes execution.

    Parameters:
    ----------
    message : str
        The message to be spoken when the function finishes. Default is "Task completed".

    Returns:
    -------
    Callable
        The decorated function with an added post-execution voice announcement.

    Example:
    -------
    >>> @notify_when_done("Done processing!")
    >>> def some_function():
    >>>     # some time-consuming task
    >>>     ...

    >>> some_function()  # Will announce "Done processing!" when completed
    """
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
    """
    A context manager that announces a start message when entering the block
    and a done message when exiting.

    Useful for wrapping code blocks where you want audible feedback at the beginning
    and end of execution.

    Parameters:
    ----------
    start : str
        Message to announce at the start of the block.
    done : str
        Message to announce when exiting the block.

    Example:
    -------
    >>> with speak("Beginning task", "Finished task"):
    >>>     # do something time-consuming
    >>>     time.sleep(5)

    This will say "Beginning task" at the start and "Finished task" when done.
    """
    say(start)
    try:
        yield
    finally:
        say(done)

def beep():
    """
    Emits a short beep sound appropriate for the current platform.

    - On **Windows**, uses `winsound.Beep` with a frequency of 1000 Hz for 200 ms.
    - On **macOS (Darwin)**, plays the system's 'Glass' sound via `afplay`.
    - On **Linux**, triggers the terminal bell using `print("\a")`.

    If an error occurs (e.g. missing sound player), it logs a failure message.

    Example:
    --------
    >>> beep()
    """
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

def play_sound_deprecated(path: str = None):
    """
    (Deprecated) Attempts to play a sound using legacy or previously bundled methods.

    Parameters
    ----------
    path : str, optional
        The absolute path to a sound file. If not provided, it attempts to play
        a default alert sound from the `assets/alert.mp3` location relative to this file.

    Notes
    -----
    - This function is deprecated and retained for backward compatibility.
    - The original method relied on `playsound`, which is no longer used.
    - No sound will be played as the implementation is currently commented out.
    - Use `play_sound()` instead for platform-specific sound playback.

    Example
    -------
    >>> play_sound_deprecated("/path/to/alert.mp3")
    """
    try:
        if not path:
            # Use default bundled sound
            path = os.path.join(os.path.dirname(__file__), "assets", "alert.mp3")
        
        path = os.path.abspath(path)
        #playsound(path)
    except Exception as e:
        print(f"[blurt] Sound failed: {e}")

def play_sound(path: str = None):
    """
    Plays a sound file appropriate to the platform.

    Parameters
    ----------
    path : str, optional
        The full path to the sound file to be played. If not provided,
        a default bundled sound (`assets/alert.mp3`) will be used.

    Platform Behavior
    -----------------
    - **Windows**: Uses `winsound.PlaySound`.
    - **macOS**: Uses `afplay` command-line tool.
    - **Linux**: Uses `aplay` command-line tool.

    Notes
    -----
    - The provided file must be supported by the system’s native player.
    - Ensure `aplay` (Linux) or `afplay` (macOS) is installed.
    - This function does not validate the audio format of the file.
    
    Example
    -------
    >>> play_sound("path/to/alert.wav")
    """
    try:
        system = platform.system()
        if not path:
            path = os.path.join(os.path.dirname(__file__), "assets", "alert.mp3")

        if system == "Windows":
            import winsound
            winsound.PlaySound(path, winsound.SND_FILENAME)
        elif system == "Darwin":
            subprocess.run(["afplay", path])
        elif system == "Linux":
            subprocess.run(["aplay", path])
    except Exception as e:
        print(f"[blurt] Sound failed: {e}")

