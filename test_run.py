from blurt import say, notify_when_done

say("This is a test message!")

@notify_when_done("Function finished!")
def some_task():
    for _ in range(3):
        print("Working...")

some_task()
