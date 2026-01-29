"""Low-level serial communication with Reachy Eyes hardware.
This module handles device discovery and raw command transmission.
"""
import time
from typing import Optional
import serial
from serial.tools import list_ports


class EyesDevice:
    """Serial interface to Reachy Mini Eyes hardware."""
    
    VID = 0x2E8A
    PID = 0x10FC
    DEVICE_ID = "REACHY_MINI_EYES"
    BAUD = 115200
    
    def __init__(self, port: str):
        """Initialize connection to eyes device.
        
        Args:
            port: Serial port path (e.g., '/dev/ttyACM0')
        
        Note:
            This is called internally by discover(). Apps should not 
            instantiate directly.
        """
        self._serial = serial.Serial(port, self.BAUD, timeout=0.3)
        time.sleep(0.15)  # Let device settle
    
    def send_command(self, cmd: str) -> None:
        """Send command to device (non-blocking, fire-and-forget).
        
        Args:
            cmd: Command string (newline will be added)
        """
        try:
            self._serial.write((cmd + "\n").encode("utf-8"))
        except Exception:
            # Fire-and-forget: silent failure
            pass
    
    def get_status(self) -> Optional[str]:
        """Request device status.
        
        Returns:
            Device ID and version string, or None if no response
        """
        try:
            # Flush any stale responses
            self._serial.reset_input_buffer()
            
            # Wait for async "OK" responses to arrive and be discarded
            time.sleep(0.2)
            
            # Send STATUS
            self._serial.write(b"STATUS\n")
            time.sleep(0.1)
            
            # Read response
            response = self._serial.readline().decode(errors="ignore").strip()
            return response if response else None
        except Exception:
            return None
    
    def wait_ready(self, timeout: float = 2.0) -> bool:
        """Poll STATUS until firmware responds, confirming it's ready.
        
        Args:
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if device responds with valid STATUS, False on timeout
        """
        start = time.time()
        
        while time.time() - start < timeout:
            status = self.get_status()
            
            # Validate we got the actual device ID, not just "OK"
            if status and self.DEVICE_ID in status:
                #print(f"[reachy-eyes] Device Ready", flush=True)
                return True
        
        return False
    
    def close(self) -> None:
        """Close serial connection."""
        try:
            self._serial.close()
        except Exception:
            pass
    
    @classmethod
    def discover(cls) -> "EyesDevice":
        """Auto-discover and connect to Reachy Eyes device."""
        for port_info in list_ports.comports():
            if port_info.vid == cls.VID and port_info.pid == cls.PID:
                try:
                    device = cls(port_info.device)
                    status = device.get_status()
                    if status and cls.DEVICE_ID in status:
                        print(f"[reachy-eyes] Connected: {status}", flush=True)
                        return device
                    device.close()
                except Exception:
                    continue
        
        raise RuntimeError(
            f"Reachy Mini Eyes not found. "
            f"Check USB connection and ensure device VID:PID is {cls.VID:04X}:{cls.PID:04X}"
        )