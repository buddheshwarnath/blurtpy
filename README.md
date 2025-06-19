# blurtpy

**Let your Python scripts speak out loud.**  
A cross-platform voice notification utility for developers, built with care under [BrinByte](https://github.com/BrinByte).

---

## 🔊 Features

- `say(text)` — Speak a message on macOS, Windows, or Linux
- `@notify_when_done()` — Automatically announce when a function finishes
- `with speak(...)` — Context manager for voice-wrapped code blocks
- Mute mode via `BLURT_MUTE=true`
- CLI support: `python -m blurt "Hello world!"`

---

## 📦 Install

```bash
pip install blurtpy
```

---
## 📦 Linux users
You’ll also need to install espeak for voice output:
```bash
sudo apt install espeak
```
If espeak is not available, blurtpy will gracefully fall back to text output with a helpful warning.    

```bash
from blurt import say, notify_when_done, speak

say("Hello developer!")

@notify_when_done("Function complete")
def task():
    ...

with speak("Starting work", done="Work done"):
    ...
```