import pytest
from core import commands

def test_shutdown_windows(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Windows")
    cmd = commands.shutdown_windows(0)
    assert cmd == "shutdown /s /t 0"

def test_abort_windows(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Windows")
    cmd = commands.abort_windows()
    assert cmd == "shutdown /a"

def test_shutdown_linux(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Linux")
    cmd = commands.shutdown_linux(0)
    assert cmd == "sudo shutdown -h 0"

def test_abort_linux(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Linux")
    cmd = commands.abort_linux()
    assert cmd == "sudo shutdown -c"

def test_current_os_linux(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Linux")
    assert commands.current_os() == "Linux"

def test_current_os_windows(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Windows")
    assert commands.current_os() == "Windows"