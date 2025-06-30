Platform Notes
==============

blurtpy works on macOS, Linux, and Windows, using platform-specific tools for speech and sound.

macOS
-----
- Uses `say` for TTS and `afplay` for sound playback (both pre-installed)
- Voices can be listed and selected
- No extra dependencies required

Linux
-----
- Uses `espeak` or `spd-say` for TTS, and `aplay` for sound
- You may need to install these tools:

  .. code-block:: bash

      sudo apt install espeak aplay

- Voice selection depends on installed voices
- If tools are missing, blurtpy will print a warning and fallback to printing

Windows
-------
- Uses `pyttsx3` for TTS and `winsound` for sound
- Voice selection depends on installed SAPI voices
- No extra dependencies required (pyttsx3 is installed automatically)

Troubleshooting
---------------
- If you hear no sound, check your system volume and that required tools are installed
- For Linux, ensure `espeak` and `aplay` are available
- For custom voices, check your OS documentation for available voices

See :doc:`configuration` for more on voice and sound options. 