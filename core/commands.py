import os
import platform

def shutdown_windows(timer):
    os.system(f"shutdown /s /t {timer}")

def abort_windows():
    os.system("shutdown /a")

def shutdown_linux(timer):
    os.system(f"sudo shutdown -h {timer}")

def abort_linux():
    os.system("sudo shutdown -c")

def current_os():
    return platform.system()