from setuptools import setup
from setuptools.command.install import install
import platform
import subprocess

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        if platform.system() == 'Linux':
            if subprocess.run(["which", "espeak"], capture_output=True).returncode != 0:
                print("\\n[blurt] Voice not available on Linux.")
                print("To enable sound, run: sudo apt install espeak\\n")

setup()
