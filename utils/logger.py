import os
from datetime import datetime

class Logger:
    def __init__(self, log_dir="logs", log_file="app.log"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(self.log_dir, log_file)

    def log(self, message: str):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        full_msg = f"{timestamp} {message}"
        print(full_msg)
        with open(self.log_file, "a") as f:
            f.write(full_msg + "\n")
