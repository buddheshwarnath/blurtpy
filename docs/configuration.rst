Configuration
=============

blurtpy supports flexible configuration via user-passed dictionaries, environment variables, and defaults.

Configurable Keys
-----------------
- `rate` (int): Words per minute (default: 200)
- `volume` (float): Volume (0.0 to 1.0, default: 1.0)
- `voice` (str): Voice identifier (system-dependent)
- `pitch` (int): Optional pitch control (platform-dependent)
- `language` (str): Language code (platform-dependent)

Configuration Priority
---------------------
1. **User config**: Passed directly to `Blurt()`
2. **Environment config**: Set `BLURT_CONFIG` as a JSON string
3. **Default config**: Used if nothing else is set

Examples
--------

User config:
.. code-block:: python

    from blurt import Blurt
    b = Blurt({"rate": 180, "volume": 0.5, "voice": "Alex"})

Environment config:
.. code-block:: bash

    export BLURT_CONFIG='{"rate": 180, "volume": 0.5, "voice": "Alex"}'

Default config:
If neither user nor environment config is set, defaults are used.

Mute All Output
---------------
Set `BLURT_MUTE=true` to silence all speaking and sound output.

See :doc:`api` for how config affects each function. 