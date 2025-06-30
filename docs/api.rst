API Reference
=============

This page documents all public functions and classes provided by the `blurt` package.

.. automodule:: blurt
    :members:
    :undoc-members:
    :show-inheritance:

Global Functions
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

beep()
~~~~~~~

Plays a short beep sound.

- **Platform-specific behavior**:
  - macOS: plays a system sound
  - Windows: uses `winsound.Beep`
  - Linux: uses `aplay` or prints ASCII bell (`\a`)

play_sound(path: str = None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plays a custom sound file.

- **Parameters**:  
  `path` (str, optional): Path to `.mp3` or `.wav` file. If omitted, default sound is used.
- **Platform-specific behavior**:
  - macOS: uses `afplay`
  - Windows: uses `winsound.PlaySound`
  - Linux: uses `aplay`

list_voices() -> List[str]
~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of available system voices.

notify_when_done(message: str = "Task completed")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A decorator that speaks a message when a function finishes executing.

- **Parameters**:  
  `message` (str): The message to announce when the function completes.
- **Usage**:  
  Use `@notify_when_done("All done!")` before your function.

announce_during(start: str = "Started", end: str = "Completed")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Context manager to announce the beginning and end of a block of code.

- **Parameters**:
  - `start` (str): Message spoken before the block runs.
  - `end` (str): Message spoken after the block finishes.

Class-based API
---------------

Blurt(config: dict = None)
~~~~~~~~~~~~~~~~~~~~~~~~~~

A class for advanced and configurable voice/sound notifications.

- **Parameters**:
  - `config` (dict, optional): Configuration for rate, volume, voice, pitch, language.
- **Methods**:
  - `say(message: str)`
  - `beep()`
  - `play_sound(path: str = None)`
  - `list_voices() -> List[str]`
  - `set_rate(rate: int)`
  - `set_volume(volume: float)`
  - `set_voice(voice: str)`

See :doc:`configuration` for all config options.

