import sys
import random
import time
from _runner import run


def demo(eyes, duration=None):

    # Determine region
    region = None
    if len(sys.argv) > 1:
        region = sys.argv[1].lower()

    if region not in {"fr", "us"}:
        region = random.choice(["fr", "us"])

    # Region-flavored message
    if region == "fr":
        print("Ça sent le roussi...\n")
    else:
        print("Someone's in trouble...\n")

    end = None if duration is None else time.time() + duration

    while end is None or time.time() < end:
        if region == "fr":
            eyes.pinpon(duration=5)
        else:
            eyes.weewoo(duration=5)

        # brief pause so it doesn't look too mechanical
        time.sleep(0.1)


if __name__ == "__main__":
    run(demo)

