from blurt import say, notify_when_done, speak

def test_say_runs():
    try:
        say("Test message", mute=False)
        assert True
    except Exception:
        assert False

def test_mute_say_runs():
    try:
        say("Mute message", mute=True)
        assert True
    except Exception:
        assert False

def test_notify_when_done_decorator():
    @notify_when_done("Done running test")
    def dummy():
        return 123

    assert dummy() == 123

def test_speak_context_manager():
    try:
        with speak("Started the process", done="Ended the process"):
            x = 1 + 1
        assert True
    except Exception:
        assert False
