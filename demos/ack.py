import time
from _runner import run


def demo(eyes, duration=None):
    end = None if duration is None else time.time() + duration
    print("Sending repeated ack() pulses\n")
    eyes.set_color("CYAN")

    while end is None or time.time() < end:
        eyes.ack()
        time.sleep(0.5)


if __name__ == "__main__":
    run(demo)

