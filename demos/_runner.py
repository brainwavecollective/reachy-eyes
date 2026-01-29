# demos/_runner.py

import sys
import signal
from pathlib import Path


def run(demo_fn):
    """Boot the eyes component and run a demo function."""
    component_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(component_dir))

    import reachy_eyes
    eyes = reachy_eyes.create({"simulation": False})

    if not eyes:
        print("Eyes not available")
        return

    def shutdown(sig, frame):
        print("\nShutting down...")
        eyes.cleanup()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)

    try:
        demo_fn(eyes)
    finally:
        eyes.cleanup()
