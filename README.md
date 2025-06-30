# 🔊 blurtpy

**Offline, cross-platform Python text-to-speech and sound notifications. 100% local, privacy-friendly, and works without internet.**

[![PyPI version](https://img.shields.io/pypi/v/blurtpy.svg)](https://pypi.org/project/blurtpy/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/buddheshwarnath/blurtpy/test.yml?branch=master)](https://github.com/buddheshwarnath/blurtpy/actions)
[![Documentation Status](https://readthedocs.org/projects/blurtpy/badge/?version=latest)](https://blurtpy.readthedocs.io/en/latest/)

---

## ✨ Features

- 🗣️ **Offline Text-to-Speech (TTS)**: Speak messages aloud on any platform, no internet required
- 🔔 **Sound Alerts**: Play system or custom sounds, 100% locally
- ✅ **Decorators**: Announce when a function completes
- 🔄 **Context Managers**: Announce start and finish of code blocks
- 🗂️ **Class-based API**: Full control over voice, rate, volume, and more
- 🧩 **Configurable**: Set rate, volume, voice, pitch, and language (user/env/default)
- 🔒 **Privacy-first**: No data sent to the cloud, works in air-gapped environments
- 🧪 **Fully tested**: Windows, macOS, Linux (CI + Docker)
- 🔇 **Mute mode**: Set `BLURT_MUTE=true` to silence all output
- 🧠 **Extensible**: Easy to add new drivers or notification types

---

## 🔒 100% Offline & Privacy-Friendly

- All features work entirely on your device—no internet connection required.
- No data is sent to the cloud. Your messages and sounds stay private.
- Perfect for secure environments, air-gapped systems, and privacy-conscious users.

---

## 📦 Installation

```bash
pip install blurtpy
```
Or with Pipenv:
```bash
pipenv install blurtpy
```

---

## 🚀 Quick Examples

```python
from blurt import say, beep, play_sound, notify_when_done, announce_during, Blurt

say("This task has started!")
beep()
play_sound()  # Plays default alert sound

@notify_when_done("All done!")
def compute():
    for i in range(3):
        print("Working...", i)
compute()

with announce_during("Start", "Finished"):
    print("Doing something long...")

# Instance-based API
b = Blurt({"rate": 250, "volume": 0.7})
b.say("Custom rate and volume!")
```

---

## 🧩 Configuration

- **User config**: Pass a dict to `Blurt()`
- **Environment config**: Set `BLURT_CONFIG` as a JSON string
- **Default config**: Used if nothing else is set

Configurable keys: `rate`, `volume`, `voice`, `pitch`, `language`

```bash
export BLURT_CONFIG='{"rate": 180, "volume": 0.5, "voice": "Alex"}'
```

---

## 🛠️ Global API

- `say(message: str)` — Speak a message aloud (offline)
- `beep()` — Play a beep sound (offline)
- `play_sound(path: str = None)` — Play a sound file (offline)
- `list_voices()` — List available system voices
- `notify_when_done(message: str)` — Decorator to announce after function completes
- `announce_during(start: str, end: str)` — Context manager to announce start/end

---

## 🏗️ Class-based API

```python
from blurt import Blurt
b = Blurt({"rate": 200, "volume": 0.8, "voice": "Samantha"})
b.say("Hello from Blurt instance!")
b.beep()
b.play_sound()
voices = b.list_voices()
b.set_rate(300)
b.set_volume(0.5)
b.set_voice("Alex")
```

---

## 🖥 Platform Support

| OS        | Voice Tool            | Sound Tool         |
|-----------|----------------------|--------------------|
| macOS     | `say`                | `afplay`           |
| Linux     | `espeak`/`spd-say`   | `aplay`            |
| Windows   | `pyttsx3`            | `winsound`         |

**Linux users:** You may need:
```bash
sudo apt install espeak aplay
```

---

## 🧪 Testing & CI

- Full test suite: `pytest -v`
- Linux tests: `docker build -f Dockerfile.linux -t blurtpy-linux-test . && docker run --rm blurtpy-linux-test`
- Cross-platform CI: GitHub Actions for Windows, macOS, Linux

---

## 🧠 Environment Variables

| Variable      | Description              | Example      |
|---------------|--------------------------|--------------|
| `BLURT_MUTE`  | Mute all output          | `true`       |
| `BLURT_CONFIG`| JSON config for Blurt    | '{"rate": 180, "voice": "Alex"}' |

---

## 📚 Documentation

Full docs: [blurtpy.readthedocs.io](https://blurtpy.readthedocs.io/en/latest/)

---

## 👨‍💻 Maintainer

Author: [Buddheshwar Nath Keshari](mailto:buddheshwar.nk@gmail.com)

---

## 📝 License

MIT License
