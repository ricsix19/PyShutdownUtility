import pytest
from core import platform_utils

def test_platform_detection_windows(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Windows")
    assert platform_utils.ensure_os("Windows") == True
    assert platform_utils.ensure_os("Linux") == False

def test_platform_detection_linux(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Linux")
    assert platform_utils.ensure_os("Linux") == True
    assert platform_utils.ensure_os("Windows") == False