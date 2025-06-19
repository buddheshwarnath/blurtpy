Changelog
=========

This document lists notable changes and updates to the `blurt` Python package across versions.

Version 0.2.2 (June 2025)
-------------------------

- ✅ Improved compatibility across platforms by removing unused `playsound` and `pyobjc` dependencies.
- ✅ Fixed installation issues on Linux/macOS due to unnecessary `pyttsx3` requirement.
- ✅ Added `blurt` as the actual module name while keeping the package name as `blurtpy`.
- ✅ Enhanced error messages and fallback behaviors when audio tools are missing.
- ✅ Added support for `beep()` and better sound playback fallbacks.

Version 0.2.1 (June 2025)
-------------------------

- ✅ Introduced platform-specific audio routing: `say` on macOS, `espeak`/`spd-say` on Linux, `pyttsx3` on Windows.
- ✅ Added context manager `speak()` and decorator `notify_when_done()` to improve developer ergonomics.
- ✅ Introduced `BLURT_MUTE` environment variable to silence output globally.
- ✅ Included fallback print outputs when sound fails.

Version 0.2.0 (Initial Public Release)
--------------------------------------

- ✅ First public release on PyPI.
- ✅ Included `say`, `play_sound`, and basic cross-platform logic.
- ✅ Included alert asset for sound notification.
- ✅ Added basic `README.md`, `setup.cfg`, and documentation framework.
