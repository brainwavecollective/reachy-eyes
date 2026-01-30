# demos/chaos.py

import time
import random
from _runner import run


COLORS = ["RED", "GREEN", "BLUE", "CYAN", "MAGENTA", "AMBER"]


def demo(eyes, duration=None):
    end = None if duration is None else time.time() + duration

    print("Chaotic mix: per-eye colors, winks, pulses, breathing\n")

    eyes.set_energy(0.8)

    next_left_color = 0
    next_right_color = 0

    while end is None or time.time() < end:
        now = time.time()

        # Rapid independent color snaps
        if now >= next_left_color:
            eyes.set_color(
                random.choice(COLORS),
                eye="LEFT",
                duration=random.uniform(0.0, 0.3),
            )
            next_left_color = now + random.uniform(0.2, 0.6)

        if now >= next_right_color:
            eyes.set_color(
                random.choice(COLORS),
                eye="RIGHT",
                duration=random.uniform(0.0, 0.3),
            )
            next_right_color = now + random.uniform(0.2, 0.6)

        r = random.random()

        # Mostly winks
        if r < 0.10:
            eyes.blink(eye=random.choice(["LEFT", "RIGHT"]))

        # Occasional ack pulses
        elif r < 0.16:
            eyes.ack()

        # Rare startle spikes
        elif r < 0.18:
            eyes.startle()

        time.sleep(0.04)

    # Restore baseline
    eyes.set_energy(0.0)


if __name__ == "__main__":
    run(demo)

