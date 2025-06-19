Frequently Asked Questions (FAQ)
================================

Here are some common questions, issues, and their solutions for using `blurt`.

Why is nothing being spoken?
----------------------------

- Check if the environment variable `BLURT_MUTE` is set. If it is set to `true`, `1`, or `yes`, speech will be disabled.
- On Linux, ensure that `espeak` or `spd-say` is installed. You can install with:

  .. code-block:: bash

      sudo apt install espeak

- On Windows, make sure `pyttsx3` is working correctly and that its dependencies (like `pypiwin32`) are installed.
- On macOS, the built-in `say` command should work. Try running `say Hello` in your terminal to verify system support.

How do I mute all speech globally?
----------------------------------

Set an environment variable before running your script:

.. code-block:: bash

    export BLURT_MUTE=true

Or within Python:

.. code-block:: python

    import os
    os.environ["BLURT_MUTE"] = "true"

Can I use `blurt` in a long script to announce progress?
--------------------------------------------------------

Yes! Use `@notify_when_done` or the `speak` context manager. Example:

.. code-block:: python

    from blurt import notify_when_done

    @notify_when_done("File processed")
    def process_file():
        ...

What if I want to play a sound instead of speech?
--------------------------------------------------

Use the `play_sound()` function. You can provide your own audio file:

.. code-block:: python

    from blurt import play_sound
    play_sound("path/to/sound.mp3")

If you don't pass a path, a default alert sound will be played (if bundled).

How do I know if sound support is available?
--------------------------------------------

On Linux, `blurt` checks for `espeak` or `spd-say`. If neither is found, it will show a warning.

On Windows/macOS, if a system command or library is unavailable, the function prints an error instead of crashing.

Does this work in Jupyter notebooks?
------------------------------------

It can, but `stdout`-based sound (like `\a`) is more reliable. GUI-based sound may not work due to subprocess limitations in Jupyter environments.

Where can I report issues or contribute?
----------------------------------------

You can open issues, contribute code, or suggest ideas at the GitHub repository:

`https://github.com/brinbyte/blurtpy <https://github.com/brinbyte/blurtpy>`_
