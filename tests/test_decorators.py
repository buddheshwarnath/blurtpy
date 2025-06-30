
import time
from blurt import notify_when_done, announce_during

def test_notify_when_done(capsys):
    @notify_when_done("All done!")
    def dummy_task():
        time.sleep(0.1)
    dummy_task()
    captured = capsys.readouterr()
    assert "All done!" in captured.out or "All done!" in captured.err

def test_announce_during_context(capsys):
    with announce_during("Starting...", "Finished..."):
        time.sleep(0.1)
    captured = capsys.readouterr()
    assert "Starting..." in captured.out or "Starting..." in captured.err
    assert "Finished..." in captured.out or "Finished..." in captured.err
