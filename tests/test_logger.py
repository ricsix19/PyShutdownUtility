import os
import tempfile
from utils.logger import Logger

def test_logger_writes_message():
    with tempfile.TemporaryDirectory() as tmpdir:
        log = Logger(log_dir=tmpdir, log_file="test.log")
        log.log("Test message")
        log_path = os.path.join(tmpdir, "test.log")
        with open(log_path) as f:
            content = f.read()
        assert "Test message" in content