import time
from unittest.mock import patch
from blurt import notify_when_done, announce_during

def test_notify_when_done():
    with patch("blurt.core.global_blurt.global_blurt.say") as mock_say:
        @notify_when_done("All done!")
        def dummy_task():
            time.sleep(0.1)
        dummy_task()
        mock_say.assert_called_with("All done!")

def test_announce_during_context():
    with patch("blurt.core.global_blurt.global_blurt.say") as mock_say:
        with announce_during("Starting...", "Finished..."):
            time.sleep(0.1)
        mock_say.assert_any_call("Starting...")
        mock_say.assert_any_call("Finished...")
