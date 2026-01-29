import time
from _runner import run


def demo(eyes, duration=None):
    end = None if duration is None else time.time() + duration
    print("Snap color transitions using set_color() with 0.0 duration\n")

    colors = ["RED", "CYAN", "AMBER", "MAGENTA", "BLUE", "GREEN"]

    while end is None or time.time() < end:
        for color in colors:
            eyes.set_color(color, duration=0.0)
            print(f"⚡ {color}")
            time.sleep(1)


if __name__ == "__main__":
    run(demo)

