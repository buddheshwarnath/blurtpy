from . import say
import sys

def main():
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
        say(message)
    else:
        print("Usage: python -m blurt 'Your message here'")

if __name__ == "__main__":
    main()
