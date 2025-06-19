# 🔊 blurt

**Speak your Python code aloud.**  
Cross-platform voice alerts for long-running tasks, decorators for completion, and built-in sound support.

[![PyPI version](https://img.shields.io/pypi/v/blurtpy.svg)](https://pypi.org/project/blurtpy/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/brinbyte/blurtpy/test.yml?branch=master)](https://github.com/brinbyte/blurtpy/actions)
[![Documentation Status](https://readthedocs.org/projects/blurtpy/badge/?version=latest)](https://blurtpy.readthedocs.io/en/latest/)

---

## ✨ Features

- 🗣️ `say("text")` — speak out messages
- ✅ `@notify_when_done()` — decorator to announce task completion
- 🔄 `with speak():` — context manager to announce start and finish
- 🔔 `beep()` and `play_sound()` — cross-platform alert sounds
- 🧪 Fully tested on Windows, macOS, Linux
- 🔇 Set `BLURT_MUTE=true` to silence everything but still log output

---

## 📦 Installation

Install with pip:

```bash
pip install blurt
```

Or with Pipenv:

```bash
pipenv install blurt
```

---

## 🚀 Quick Examples

```python
from blurt import say, beep, notify_when_done, speak

say("This task has started")

@notify_when_done("All done!")
def compute():
    for i in range(3):
        print("Working...", i)

compute()

with speak("Start", "Finished"):
    # Do something long
    pass

beep()
```

---

## 📚 Full Documentation

📖 Read the full docs at [blurtpy.readthedocs.io](https://blurtpy.readthedocs.io/en/latest/)

---

## 🖥 Platform Notes

| OS       | Voice Tool            | Sound Tool         |
|----------|------------------------|--------------------|
| **macOS** | `say`                 | `afplay`           |
| **Linux** | `espeak` / `spd-say`  | `aplay`            |
| **Windows** | `pyttsx3`             | `winsound`         |

**Linux users**: You may need:

```bash
sudo apt install espeak aplay
```

---

## 🧪 Tests

This project is tested across:

- ✅ Python 3.10
- ✅ Windows / Linux / macOS (via GitHub Actions)
- ✅ Manual sound tests via CI-supported environments

---

## 🧠 Environment Variables

| Variable      | Description              | Example      |
|---------------|--------------------------|--------------|
| `BLURT_MUTE`  | Mute voice output        | `true`       |

---

## 🔖 Version

Current release: `0.2.2`

---

## 👨‍💻 Maintainers

Author: [Buddheshwar Nath Keshari](mailto:buddheshwar.nk@gmail.com)

---

## 📝 License

This project is licensed under the MIT License.
