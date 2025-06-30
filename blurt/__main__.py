"""
blurt.__main__ - CLI entry point for blurtpy

Usage examples:
  python -m blurt say "Hello world"
  python -m blurt beep
  python -m blurt sound path/to/file.mp3
  python -m blurt list-voices
  python -m blurt say "Hi" --rate 180 --volume 0.8
"""

import argparse
import json
import os
from blurt import say, beep, play_sound
from blurt.core.blurt import Blurt
from blurt.core.voice_config import VoiceConfig

def parse_config(args) -> VoiceConfig:
    """
    Build voice config from command-line args or BLURT_CONFIG.
    CLI args take priority over env.
    """
    env_config = os.getenv("BLURT_CONFIG")
    config_dict = {}

    if env_config:
        try:
            config_dict = json.loads(env_config)
        except json.JSONDecodeError:
            print("[blurt] Invalid JSON in BLURT_CONFIG")

    # Override from CLI if provided
    if args.rate is not None:
        config_dict["rate"] = args.rate
    if args.volume is not None:
        config_dict["volume"] = args.volume
    if args.voice is not None:
        config_dict["voice"] = args.voice

    return VoiceConfig.from_dict(config_dict)

def main():
    parser = argparse.ArgumentParser(prog="blurt", description="Cross-platform voice notifier")
    subparsers = parser.add_subparsers(dest="command", help="blurt commands")

    # say command
    say_parser = subparsers.add_parser("say", help="Speak a message aloud")
    say_parser.add_argument("message", nargs="+", help="Message to speak")
    say_parser.add_argument("--rate", type=int, help="Speech rate (words per minute)")
    say_parser.add_argument("--volume", type=float, help="Volume (0.0 to 1.0)")
    say_parser.add_argument("--voice", type=str, help="Voice identifier (if supported)")

    # beep command
    subparsers.add_parser("beep", help="Play system beep")

    # sound command
    sound_parser = subparsers.add_parser("sound", help="Play sound file")
    sound_parser.add_argument("path", help="Path to sound file")

    # list-voices command
    subparsers.add_parser("list-voices", help="List available voices")

    args = parser.parse_args()

    if args.command == "say":
        config = parse_config(args)
        Blurt(config.as_dict()).say(" ".join(args.message))
    elif args.command == "beep":
        beep()
    elif args.command == "sound":
        play_sound(args.path)
    elif args.command == "list-voices":
        voices = Blurt().list_voices()
        if voices:
            print("\nAvailable voices:")
            for v in voices:
                print(" -", v)
        else:
            print("[blurt] No voices found or not supported on this platform.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
