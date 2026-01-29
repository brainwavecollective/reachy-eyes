"""Firmware protocol constants and command definitions.

This module defines the command interface for the Reachy Mini Eyes firmware.
It provides type-safe constants for colors, configuration parameters, and effects.
"""


class Color:
    """Named colors supported by the firmware."""
    WHITE = "WHITE"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    AMBER = "AMBER"
    CYAN = "CYAN"
    MAGENTA = "MAGENTA"
    OFF = "OFF"


class Config:
    """Configuration parameters that can be persisted to NVM."""
    BRIGHTNESS = "BRIGHTNESS"
    COLOR_TAU = "COLOR_TAU"
    DEFAULT_INTENSITY = "DEFAULT_INTENSITY"
    DEFAULT_ENERGY = "DEFAULT_ENERGY"
    DEFAULT_ASYMMETRY = "DEFAULT_ASYMMETRY"
    BLINK_DUR_MS = "BLINK_DUR_MS"
    BLINK_DEPTH = "BLINK_DEPTH"
    ACK_AMP = "ACK_AMP"
    ACK_DUR_MS = "ACK_DUR_MS"
    STARTLE_AMP = "STARTLE_AMP"
    STARTLE_DUR_MS = "STARTLE_DUR_MS"
    STARTLE_ENERGY_BOOST = "STARTLE_ENERGY_BOOST"


class Effect:
    """Effect commands."""
    BLINK = "BLINK"
    ACK = "ACK"
    STARTLE = "STARTLE"


class Eye:
    """Eye identifiers for per-eye commands."""
    LEFT = "L"
    RIGHT = "R"
