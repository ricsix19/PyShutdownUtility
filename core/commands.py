import os
import platform

def shutdown_windows(timer):
    os.system(f"shutdown /s /t {timer}")

def abort_windows():
    os.system("shutdown /a")