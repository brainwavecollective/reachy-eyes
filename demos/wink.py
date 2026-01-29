# wink.py
import time
import random
from _runner import run


def demo(eyes, duration=None):
    end = None if duration is None else time.time() + duration
    print("Random eyes blink() with left/right/both, random timings\n")

    eyes.set_color("CYAN")

    choices = ["LEFT", "RIGHT", None]

    while end is None or time.time() < end:
        eye = random.choice(choices)

        if eye is None:
            eyes.blink()  # both
        else:
            eyes.blink(eye=eye)

        # Random pause between winks
        time.sleep(random.uniform(0.8, 3.2))


if __name__ == "__main__":
    run(demo)

