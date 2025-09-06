import os
import platform

def shutdown_windows(timer: int) -> str:
    return f"shutdown /s /t {timer}"

def abort_windows() -> str:
    return "shutdown /a"

def shutdown_linux(timer: int) -> str:
    return f"sudo shutdown -h {timer}"

def abort_linux() -> str:
    return "sudo shutdown -c"

def execute_command(command: str):
    os.system(command)

def current_os() -> str:
    return platform.system()