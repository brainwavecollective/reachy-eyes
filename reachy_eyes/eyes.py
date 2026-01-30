"""High-level API for Reachy Mini Eyes."""

import random
import time
import threading
from typing import Optional

from .protocol import Color, Config, Effect, Eye
from .defaults import CFG_PARAMS, RUNTIME_STATE, HOST_DEFAULTS

_EYE_ALIASES = {
    "L": Eye.LEFT,
    "R": Eye.RIGHT,
    "LEFT": Eye.LEFT,
    "RIGHT": Eye.RIGHT,
}


class ReachyEyes:
    """High-level interface to Reachy Mini Eyes."""

    def __init__(self, device):
        self._device = device
        self._initialize()

        # --- Blinking state (host-side physiology) ---
        self._blinking_enabled = False
        self._blink_thread = None

        self._blink_interval_low = HOST_DEFAULTS["BLINK_INTERVAL_LOW"]
        self._blink_interval_high = HOST_DEFAULTS["BLINK_INTERVAL_HIGH"]
        self._blink_double_rate = HOST_DEFAULTS["BLINK_DOUBLE_RATE"]
        self._blink_double_gap = HOST_DEFAULTS["BLINK_DOUBLE_GAP"]

    # ===== Initialization =====

    def _initialize(self):
        from .defaults import CFG_PARAMS, RUNTIME_STATE
        
        # Configure firmware parameters
        for key, value in CFG_PARAMS.items():
            self._device.send_command(f"CFG {key} {value}")        
        time.sleep(0.3)
        
        # Verify responsiveness
        if not self._device.wait_ready(timeout=2.0):
            raise RuntimeError("Firmware did not respond after configuration")
        
        # Set initial state
        for key, value in RUNTIME_STATE.items():
            self._device.send_command(f"{key} {value}")
        
    # ===== Core Color Control =====

    def set_color(
        self,
        color: str,
        duration: Optional[float] = None,
        eye: Optional[str] = None,
    ) -> None:
        cmd = f"{color}"
        if duration is not None:
            cmd += f" {duration}"
        if eye:
            cmd = f"{self._norm_eye(eye)}:{cmd}"
        self._device.send_command(cmd)

    # ===== State Parameters =====

    def set_intensity(self, value: float, eye: Optional[str] = None) -> None:
        cmd = f"INTENSITY {value}"
        if eye:
            cmd = f"{self._norm_eye(eye)}:{cmd}"
        self._device.send_command(cmd)

    def set_energy(self, value: float, eye: Optional[str] = None) -> None:
        cmd = f"ENERGY {value}"
        if eye:
            cmd = f"{self._norm_eye(eye)}:{cmd}"
        self._device.send_command(cmd)

    def set_asymmetry(self, value: float, eye: Optional[str] = None) -> None:
        cmd = f"ASYMMETRY {value}"
        if eye:
            cmd = f"{self._norm_eye(eye)}:{cmd}"
        self._device.send_command(cmd)

    # ===== Effects =====

    def blink(self, eye: Optional[str] = None) -> None:
        cmd = Effect.BLINK
        if eye:
            cmd = f"{self._norm_eye(eye)}:{cmd}"
        self._device.send_command(cmd)

    def ack(self, eye: Optional[str] = None) -> None:
        cmd = Effect.ACK
        if eye:
            cmd = f"{self._norm_eye(eye)}:{cmd}"
        self._device.send_command(cmd)

    def startle(self, eye: Optional[str] = None) -> None:
        cmd = Effect.STARTLE
        if eye:
            cmd = f"{self._norm_eye(eye)}:{cmd}"
        self._device.send_command(cmd)

    # ===== Autonomous Behaviors =====

    def _blink_loop(self):
        import random

        while self._blinking_enabled:
            time.sleep(
                random.uniform(
                    self._blink_interval_low,
                    self._blink_interval_high,
                )
            )

            self.blink()

            if random.random() < self._blink_double_rate:
                time.sleep(self._blink_double_gap)
                self.blink()

    def enable_blinking(
        self,
        interval_low: float | None = None,
        interval_high: float | None = None,
        double_rate: float | None = None,
        double_gap: float | None = None,
    ) -> None:
        if interval_low is not None:
            self._blink_interval_low = interval_low
        if interval_high is not None:
            self._blink_interval_high = interval_high
        if double_rate is not None:
            self._blink_double_rate = double_rate
        if double_gap is not None:
            self._blink_double_gap = double_gap

        if self._blinking_enabled:
            return

        self._blinking_enabled = True
        self._blink_thread = threading.Thread(
            target=self._blink_loop,
            daemon=True,
        )
        self._blink_thread.start()

    def disable_blinking(self) -> None:
        self._blinking_enabled = False
     

    # ===== Expressive Behaviors =====
    
    def weewoo(self, duration: Optional[float] = None) -> None:
        """Alternating red/blue with strong pulses."""

        end = None if duration is None else time.time() + duration

        self.set_intensity(0.6)

        swap = True
        last_swap = time.time()

        last_left = 0.0
        last_right = 0.12 

        self.set_color("RED", eye="LEFT", duration=0.0)
        self.set_color("BLUE", eye="RIGHT", duration=0.0)

        while end is None or time.time() < end:
            now = time.time()

            if now - last_swap > 0.42:
                swap = not swap
                last_swap = now

                if swap:
                    self.set_color("RED", eye="LEFT", duration=0.0)
                    self.set_color("BLUE", eye="RIGHT", duration=0.0)
                else:
                    self.set_color("RED", eye="RIGHT", duration=0.0)
                    self.set_color("BLUE", eye="LEFT", duration=0.0)

            LEFT_INTERVAL  = 0.22
            RIGHT_INTERVAL = 0.18

            if now - last_left > LEFT_INTERVAL:
                self.startle(eye="LEFT")
                last_left = now

            if now - last_right > RIGHT_INTERVAL:
                self.startle(eye="RIGHT")
                last_right = now

            QUIET_THRESHOLD = 0.15

            if (now - last_left > QUIET_THRESHOLD) and (now - last_right > QUIET_THRESHOLD):
                # two rapid startles, both eyes
                self.startle(eye="LEFT")
                self.startle(eye="LEFT")
                self.startle(eye="LEFT")
                time.sleep(0.035)
                self.startle(eye="RIGHT")
                self.startle(eye="RIGHT")

                last_left = now
                last_right = now



    def pinpon(self, duration: Optional[float] = None) -> None:
        """3 quick pulses + break; alternate eyes each cycle."""

        end = None if duration is None else time.time() + duration

        self.set_energy(0.0)
        self.set_intensity(1.0)

        # Tune these
        on = 0.010
        off = 0.010
        gap = 0.015

        def pulse3(eye: str) -> None:
            for _ in range(3):
                self.set_color("BLUE", eye=eye, duration=0.0)
                time.sleep(on)
                self.set_color("OFF", eye=eye, duration=0.0)
                time.sleep(off)

        eye = "LEFT"

        while end is None or time.time() < end:
            pulse3(eye)
            time.sleep(gap)
            eye = "RIGHT" if eye == "LEFT" else "LEFT"



    # ===== Convenience =====

    def off(self) -> None:
        self.set_color(Color.OFF)
        
    def _norm_eye(self, eye: Optional[str]) -> Optional[str]:
        if eye is None:
            return None
        try:
            return _EYE_ALIASES[eye.upper()]
        except KeyError:
            raise ValueError(
                f"Invalid eye '{eye}'. Use L/R, LEFT/RIGHT, or Eye.LEFT/Eye.RIGHT."
            )

    # ===== Lifecycle =====

    def cleanup(self) -> None:
        self.disable_blinking()
        try:
            self.off()
            time.sleep(0.1)
        except Exception:
            pass
        finally:
            self._device.close()
