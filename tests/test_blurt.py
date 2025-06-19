from blurt import say, notify_when_done, speak, beep, play_sound

def test_say_runs():
    try:
        say("Test message")
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

def test_beep_runs():
    try:
        beep()
        assert True
    except Exception:
        assert False

def test_play_sound_fails_gracefully():
    try:
        # This should fail internally but not raise an exception
        play_sound()
        assert True
    except Exception:
        assert False
