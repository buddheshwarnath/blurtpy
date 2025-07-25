import platform
from typing import Optional, Dict, List
from blurt.drivers.base_driver import BaseDriver
from blurt.drivers.driver_macos import MacOSDriver
from blurt.drivers.driver_linux import LinuxDriver
from blurt.drivers.driver_windows import WindowsDriver

class DriverFactory:
    @staticmethod
    def get_driver(config: Dict) -> BaseDriver:
        system = platform.system()
        if system == "Darwin":
            return MacOSDriver(**config)
        elif system == "Linux":
            return LinuxDriver(**config)
        elif system == "Windows":
            return WindowsDriver(**config)
        else:
            raise RuntimeError(f"Unsupported platform: {system}")
