"""
decorators.py - Decorators and context managers for blurtpy.
Includes function notification and speech wrappers.
"""

from contextlib import contextmanager
from functools import wraps
from blurt.core.global_blurt import global_blurt
from blurt.constants import DEFAULT_START_MESSAGE, DEFAULT_END_MESSAGE


def notify_when_done(message: str = "Task completed"):
    """
    Decorator that announces a message after the decorated function completes.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            global_blurt.say(message)
            return result
        return wrapper
    return decorator


@contextmanager
def announce_during(start: str = DEFAULT_START_MESSAGE, end: str = DEFAULT_END_MESSAGE):
    """
    Context manager that announces messages before and after a code block.
    
    Example:
        with announce_during("Processing started", "Processing finished"):
            do_something()
    """
    global_blurt.say(start)
    try:
        yield
    finally:
        global_blurt.say(end)
