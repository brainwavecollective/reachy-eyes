"""Default configuration values for Reachy Mini Eyes.

These values are automatically applied when the component initializes.
They override the firmware's built-in defaults to provide consistent,
tuned behavior out of the box.

Apps can override specific values
"""


# Firmware configuration parameters (sent as CFG commands)
# These affect firmware behavior: effect timing, transition speeds, safety caps
CFG_PARAMS = {

    "COLOR_TAU": 0.4,                # Color transition smoothing time (seconds)

    "BLINK_DUR_MS": 120,             # Blink duration (milliseconds)
    "BLINK_DEPTH": 1.0,              # Blink darkness (0.0-1.0, 1.0=full blackout)

    "ACK_AMP": 0.12,                 # Ack pulse amplitude (0.0-1.0)
    "ACK_DUR_MS": 80,                # Ack pulse duration (milliseconds)

    "BRIGHTNESS": 0.42,              # DO NOT MODIFY Global brightness safety cap (0.0-1.0)

    "STARTLE_AMP": 0.6,              # Startle flash amplitude (0.0-1.0)
    "STARTLE_DUR_MS": 120,           # Startle flash duration (milliseconds)
    "STARTLE_ENERGY_BOOST": 0.0,     # Energy increase on startle (0.0-1.0)

}

# Initial runtime state (sent as direct commands on connection)
# These set the starting values for dynamic eye parameters
RUNTIME_STATE = {

    "INTENSITY": 0.87,               # Base brightness level (0.0-1.0)
    "ENERGY": 0.0,                   # Breathing/modulation depth (0.0-1.0)
    "ASYMMETRY": 0.1,                # Per-eye variation (0.0-1.0)
    "SHIMMER": 0.0,                  # Stellar scintillation effect (0.0-1.0)

}

# Host-side behavior parameters (Python module, not sent to firmware)
# These control autonomous behaviors like automatic blinking
HOST_DEFAULTS = {

    "BLINK_INTERVAL_LOW": 1.0,       # Minimum seconds between blinks
    "BLINK_INTERVAL_HIGH": 12.0,     # Maximum seconds between blinks
    "BLINK_DOUBLE_RATE": 0.13,       # Probability of double-blink (0.0-1.0)
    "BLINK_DOUBLE_GAP": 0.15,        # Seconds between double-blink

}
