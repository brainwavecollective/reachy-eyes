import time
import random
from _runner import run


def demo(eyes, duration=None):
    end = None if duration is None else time.time() + duration
    print("Random calls to blink() between 0.4 and 3 seconds\n")

    eyes.set_color("CYAN")

    while end is None or time.time() < end:
        eyes.blink()
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    run(demo)
