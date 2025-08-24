import tkinter as tk
from ui.os_window import create_os_windows
from ui.os_window import center_window

def create_main_window():
    app = tk.Tk()
    app.title("Shutdown Utility")
    app.geometry("300x250")
    app.resizable(False, False)

    tk.Label(app, text="Choose your operating system!").pack(pady=10)
    tk.Button(app, text="Windows", command=lambda: create_os_windows(app, "Windows", "Windows"), height=2, width=20).pack(pady=10)
    tk.Button(app, text="Linux", command=lambda: create_os_windows(app, "Linux", "Linux"), height=2, width=20).pack(pady=10)
    tk.Button(app, text="Exit", command=app.destroy, height=2, width=20).pack(pady=10)

    center_window(app)

    return app