import time
from _runner import run


def demo(eyes, duration=None):
    end = None if duration is None else time.time() + duration
    print("Controlling set_color() with different colors for each eye\n")

    left = ["RED", "GREEN", "BLUE"]
    right = ["CYAN", "MAGENTA", "AMBER"]

    i = 0
    while end is None or time.time() < end:
        eyes.set_color(left[i % 3], eye="LEFT", duration=2.0)
        eyes.set_color(right[i % 3], eye="RIGHT", duration=2.0)
        time.sleep(3)
        i += 1


if __name__ == "__main__":
    run(demo)

