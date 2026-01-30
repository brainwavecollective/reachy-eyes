import time
from _runner import run


def demo(eyes, duration=None):
    print("Mimicking breath with energy()\n")

    end = None if duration is None else time.time() + duration

    eyes.set_color("CYAN")

    # Raise energy
    eyes.set_energy(0.75)

    while end is None or time.time() < end:
        time.sleep(0.2)

    # Restore calm
    eyes.set_energy(0.1)

if __name__ == "__main__":
    run(demo)
