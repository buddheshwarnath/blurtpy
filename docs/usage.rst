Usage Examples
==============

Basic Speaking
--------------

Use `say()` to speak a simple message aloud:

.. code-block:: python

    from blurt import say

    say("Hello, world!")


Notify When Done (Decorator)
----------------------------

Use `@notify_when_done` to automatically speak after a function completes:

.. code-block:: python

    from blurt import notify_when_done

    @notify_when_done("Processing done!")
    def process_data():
        # Your logic here
        print("Working...")

    process_data()


Context Manager: speak()
------------------------

Use the `speak()` context manager to announce when a block of code starts and finishes:

.. code-block:: python

    from blurt import speak

    with speak("Starting task", "Finished task"):
        # Do something
        for _ in range(3):
            print("Processing...")


Beep (Cross-platform)
---------------------

Play a short system beep sound:

.. code-block:: python

    from blurt import beep

    beep()


Play Sound File
---------------

Play a custom `.mp3` or `.wav` file using your system’s default sound player:

.. code-block:: python

    from blurt import play_sound

    play_sound("/path/to/your/alert.mp3")

If no path is passed, a default alert sound (included with the package) will play.


Mute All Sounds
---------------

You can globally mute all speaking or beeping using an environment variable:

.. code-block:: bash

    export BLURT_MUTE=true

This is useful in CI, automated scripts, or when you want silent mode.


Fallback Behavior
-----------------

On platforms where sound tools like `say`, `espeak`, or `pyttsx3` are missing, the message will be printed with a mute/fallback prefix, and clear instructions will be printed (especially for Linux users).


Next
----

See :doc:`api` for detailed reference of each function.
