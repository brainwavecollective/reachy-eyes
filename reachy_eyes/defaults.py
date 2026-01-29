"""Default configuration values for Reachy Mini Eyes.

These values are automatically applied when the component initializes.
They override the firmware's built-in defaults to provide consistent,
well-tuned behavior out of the box.

Apps can override specific values using:
    eyes.configure(Config.BRIGHTNESS, 0.8)

Note: These values are sent as CFG commands on every connection.
"""

CFG_DEFAULTS = {
    # Display settings
    "COLOR_TAU": 0.4,                # Color transition smoothing time (seconds)
    
    # Default state parameters
    "DEFAULT_INTENSITY": 0.7,        # Base brightness level (0.0-1.0)
    "DEFAULT_ENERGY": 0.0,           # Breathing/modulation depth (0.0-1.0)
    "DEFAULT_ASYMMETRY": 0.1,        # Per-eye variation (0.0-1.0)
    
    # Blink effect
    "BLINK_DUR_MS": 120,             # Blink duration (milliseconds)
    "BLINK_DEPTH": 1.0,              # Blink darkness (0.0-1.0, 1.0=full blackout)
    
    # Acknowledgment effect
    "ACK_AMP": 0.12,                 # Ack pulse amplitude (0.0-1.0)
    "ACK_DUR_MS": 80,                # Ack pulse duration (milliseconds)
    
    # Startle effect
    "STARTLE_AMP": 0.6,              # Startle flash amplitude (0.0-1.0)
    "STARTLE_DUR_MS": 120,           # Startle flash duration (milliseconds)
    "STARTLE_ENERGY_BOOST": 0.0,    # Energy increase on startle (0.0-1.0)
}

# Host-side 
HOST_DEFAULTS = {
    # Natural blinking physiology, for blink background latch
    "BLINK_INTERVAL_LOW": 1.0,
    "BLINK_INTERVAL_HIGH": 12.0,
    "BLINK_DOUBLE_RATE": 0.13,
    "BLINK_DOUBLE_GAP": 0.15,
}
