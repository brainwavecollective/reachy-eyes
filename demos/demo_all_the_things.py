# demos/demo_all_the_things.py

import random
import importlib
from pathlib import Path
from _runner import run


def load_demos():
    demos = []
    here = Path(__file__).parent
    this_file = Path(__file__).stem

    for path in sorted(here.glob("*.py")):
        module_name = path.stem      # for import
        display_name = path.name    # for header

        if module_name in {"_runner", this_file}:
            continue

        module = importlib.import_module(module_name)
        fn = getattr(module, "demo", None)

        if callable(fn):
            demos.append((display_name, fn))
            print(f"Loaded demo: {display_name}")

    if not demos:
        raise RuntimeError("No demos found.")

    return demos


DEMOS = load_demos()


def print_chunk_header(name: str, dur: float):
    bar = "─" * 60
    print()
    print(bar)
    print(f"[ {name} ]  {dur:>4.1f}s")
    print(bar)


def demo(eyes, duration=None):
    print("Running all the things (shuffled cycles)\n")

    deck = []

    while True:
        if not deck:
            deck = DEMOS.copy()
            random.shuffle(deck)

        name, fn = deck.pop()
        dur = random.uniform(4, 6)

        print_chunk_header(name, dur)
        fn(eyes, duration=dur)
        print()  # ensure separation between chunks


if __name__ == "__main__":
    run(demo)

