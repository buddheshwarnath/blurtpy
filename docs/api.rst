API Reference
=============

This page documents all public functions provided by the `blurt` package.

.. automodule:: blurt
    :members:
    :undoc-members:
    :show-inheritance:


Function Details
----------------

say(message: str)
~~~~~~~~~~~~~~~~~

Speaks a message out loud using the system's speech engine.

- **Parameters**:  
  `message` (str): The message to speak.
- **Behavior**:  
  Uses `say` on macOS, `espeak` or `spd-say` on Linux, and `pyttsx3` on Windows.
- **Mute option**:  
  Set environment variable `BLURT_MUTE=true` to disable speaking.

notify_when_done(message: str = "Task completed")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A decorator that speaks a message when a function finishes executing.

- **Parameters**:  
  `message` (str): The message to announce when the function completes.
- **Usage**:  
  Use `@notify_when_done("All done!")` before your function.

speak(start: str = "Started", done: str = "Completed")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Context manager to announce the beginning and end of a block of code.

- **Parameters**:
  - `start` (str): Message spoken before the block runs.
  - `done` (str): Message spoken after the block finishes.
- **Usage**:

  .. code-block:: python

      with speak("Begin", "Done"):
          # block of code

beep()
~~~~~~

Plays a short beep sound.

- **Platform-specific behavior**:
  - macOS: plays `/System/Library/Sounds/Glass.aiff`
  - Windows: uses `winsound.Beep`
  - Linux: prints ASCII bell (`\a`)

play_sound(path: str = None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plays a custom sound file.

- **Parameters**:  
  `path` (str, optional): Path to `.mp3` or `.wav` file. If omitted, default sound is used.
- **Platform-specific behavior**:
  - macOS: uses `afplay`
  - Windows: uses `winsound.PlaySound`
  - Linux: uses `aplay`

