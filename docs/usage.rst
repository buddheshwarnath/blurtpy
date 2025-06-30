Usage Examples
==============

Basic Speaking
--------------

Use `say()` to speak a simple message aloud:

.. code-block:: python

    from blurt import say
    say("Hello, world!")

Beep (Cross-platform)
---------------------

Play a short system beep sound:

.. code-block:: python

    from blurt import beep
    beep()

Play Sound File
---------------

Play a custom `.mp3` or `.wav` file, or the default alert sound:

.. code-block:: python

    from blurt import play_sound
    play_sound()  # Default alert sound
    play_sound("/path/to/your/alert.mp3")

List Available Voices
---------------------

.. code-block:: python

    from blurt import list_voices
    voices = list_voices()
    print(voices)

Notify When Done (Decorator)
----------------------------

Use `@notify_when_done` to automatically speak after a function completes:

.. code-block:: python

    from blurt import notify_when_done

    @notify_when_done("Processing done!")
    def process_data():
        print("Working...")
    process_data()

Announce During (Context Manager)
---------------------------------

Use the `announce_during()` context manager to announce when a block of code starts and finishes:

.. code-block:: python

    from blurt import announce_during

    with announce_during("Starting task", "Finished task"):
        for _ in range(3):
            print("Processing...")

Class-based API
---------------

.. code-block:: python

    from blurt import Blurt
    b = Blurt({"rate": 250, "volume": 0.7})
    b.say("Custom rate and volume!")
    b.beep()
    b.play_sound()
    voices = b.list_voices()
    b.set_rate(300)
    b.set_volume(0.5)
    b.set_voice("Alex")

Mute All Sounds
---------------

You can globally mute all speaking or beeping using an environment variable:

.. code-block:: bash

    export BLURT_MUTE=true

See :doc:`configuration` for more options.

Next
----

See :doc:`api` for detailed reference of each function.
