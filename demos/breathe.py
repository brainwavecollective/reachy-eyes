import time
from _runner import run


def demo(eyes, duration=None):
    print("Mimicking breath with energy()\n")

    end = None if duration is None else time.time() + duration

    # Raise energy for this behavior
    eyes.set_energy(0.75)

    while end is None or time.time() < end:
        time.sleep(0.2)

    # Restore baseline physiology
    eyes.set_energy(0.0)

