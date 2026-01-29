"""Reachy Mini Eyes Component.

This component provides control of the Reachy Mini Eyes hardware through
a simple, high-level API.

Usage:
    # In app code
    eyes = robot.component["reachy-eyes"]
    if eyes:
        eyes.set_color(Color.RED)
        eyes.breathing(Color.BLUE, energy=0.8)
        eyes.flash(Color.GREEN, count=5)
"""

__version__ = "0.1.0"

from .protocol import Color, Config, Effect, Eye
from .eyes import ReachyEyes
from .device import EyesDevice


def create(context: dict | None = None):
    """Component factory function.
    
    Called by the daemon during startup to initialize the component.
    
    Args:
        context: Optional component context dictionary containing:
            - simulation (bool): Whether running in simulation mode
                (currently not supported, hardware required)
    
    Returns:
        ReachyEyes instance if hardware found, None otherwise
    
    Note:
        Component failures do not break daemon startup. If hardware
        is not found, returns None and daemon continues.
        
        Module defaults from defaults.py are automatically applied during
        initialization to ensure consistent behavior regardless of firmware
        defaults or NVM state. Apps can override specific values using
        eyes.configure() after initialization.
    """
    context = context or {}
    
    if context.get("simulation", False):
        return None
    
    try:
        device = EyesDevice.discover()
        eyes = ReachyEyes(device)  # __init__ handles all initialization
        return eyes
    except Exception as e:
        print(f"[reachy-eyes] Failed to initialize: {e}")
        return None

__all__ = [
    "__version__",
    "create",
    "ReachyEyes",
    "Color",
    "Config",
    "Effect",
    "Eye",
]