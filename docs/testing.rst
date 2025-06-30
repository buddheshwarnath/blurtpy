Testing & CI
============

blurtpy is fully tested across platforms, with automated and manual tests.

Running Tests Locally
---------------------

.. code-block:: bash

    pipenv run pytest -v

Linux Testing with Docker
-------------------------

You can run tests in a clean Linux environment using Docker:

.. code-block:: bash

    docker build -f Dockerfile.linux -t blurtpy-linux-test .
    docker run --rm blurtpy-linux-test

Continuous Integration (CI)
---------------------------
- GitHub Actions runs tests on Windows, macOS, and Linux for every commit and pull request
- PyPI publishing is automated via CI

See :doc:`platform` for platform-specific test requirements. 