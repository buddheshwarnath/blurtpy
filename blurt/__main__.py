"""
blurt.__main__ - Entry point when running the package directly.

Usage:
    python -m blurt say "Hello, world!"
    python -m blurt beep
    python -m blurt help

This script acts as a CLI wrapper around core blurt functions.
"""

import sys
from blurt import say, beep, speak

def print_help():
    print("""
blurt - Simple cross-platform text-to-speech and notifications.

Usage:
  python -m blurt say "Your message"   Speak the given message.
  python -m blurt beep                 Play a short beep.
  python -m blurt help                 Show this help message.
""")

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()

    if command == "say" and len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
        say(message)
    elif command == "beep":
        beep()
    elif command == "help":
        print_help()
    else:
        print("[blurt] Unknown command.\n")
        print_help()

if __name__ == "__main__":
    main()
