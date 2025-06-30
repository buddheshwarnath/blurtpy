"""
test_blurtpy.py - Comprehensive manual test suite for blurtpy
Run directly to verify all functionality across platforms.
"""

from blurt import say, beep, play_sound, list_voices, notify_when_done, announce_during, Blurt
import time
from blurt.constants import BEEP_SOUND_FILE

print("\n--- GLOBAL API TESTS ---\n")

print("Test: say() with default voice")
say("This is a global say test with default voice.")

print("Test: beep() with default sound")
beep()

print("Test: play_sound() with default sound")
play_sound()

def test_notify_decorator():
    @notify_when_done("Decorator: Task completed!")
    def dummy_task():
        print("Decorator: Running dummy task...")
        time.sleep(1)
    dummy_task()

test_notify_decorator()

print("Test: announce_during context manager")
with announce_during("Context: Starting block", "Context: Finished block"):
    print("Context: Doing work...")
    time.sleep(1)

print("Test: list_voices() (showing first 5)")
voices = list_voices()
print("Voices:", voices[:5])

print("\n--- INSTANCE-BASED API TESTS ---\n")

print("Test: Blurt instance with default config")
b = Blurt()
b.say("Instance: This is a test with default config.")
b.beep()
b.play_sound()

print("Test: Blurt instance with custom rate and volume")
b2 = Blurt({"rate": 300, "volume": 0.5})
b2.say("Instance: Custom rate 300, volume 0.5.")

if voices:
    print(f"Test: Blurt instance with custom voice: {voices[0]}")
    b3 = Blurt({"voice": voices[0]})
    b3.say(f"Instance: Using custom voice {voices[0]}.")

print("Test: Blurt instance with all custom params")
b4 = Blurt({"rate": 150, "volume": 0.8, "voice": voices[1] if len(voices) > 1 else None})
b4.say("Instance: Custom rate, volume, and voice.")

print("Test: Instance context manager (announce_during)")
with announce_during("Instance: Block start", "Instance: Block end"):
    b4.say("Instance: Speaking inside context manager.")
    time.sleep(1)

print("Test: play_sound() with custom file (beep.mp3)")
play_sound(BEEP_SOUND_FILE)

print("\n--- ALL TESTS COMPLETED ---\n")
