import tkinter as tk
from tkinter import messagebox
from core import commands, platform_utils

def create_os_windows(app, title, os_name):
    app.withdraw()
    window = tk.Toplevel(app)
    window.title(title)
    window.geometry("300x400")
    window.resizable(False, False)

    label = tk.Label(window, text = "Enter shutdown time (seconds):")
    label.pack(pady=10)

    timer_entry = tk.Entry(window, width = 50)
    timer_entry.pack(pady=10, padx=20)

    def shutdown():
        timer = timer_entry.get()
        if not timer.isdigit():
            messagebox.showerror("Invalid Number", "Enter a valid number")
            return

        if messagebox.askokcancel("Shutdown", "Do you really want to shutdown?"):
            if platform_utils.ensure_os(os_name):
                if os_name == "Windows":
                    cmd = commands.shutdown_windows(timer)
                else:
                    cmd = commands.shutdown_linux(timer)
            else:
                platform_utils.show_worng_os_error()
        commands.execute_command(cmd)

    def abort():
        if messagebox.askokcancel("Abort shutdown", "Do you really want to abort shutdown?"):
            if platform_utils.ensure_os(os_name):
                commands.abort_windows() if os_name == "Windows" else commands.abort_linux()
            else:
                platform_utils.show_worng_os_error()

    tk.Button(window, text="Shutdown", command=shutdown, height=2, width=20).pack(pady=10, padx=20, anchor="center")
    tk.Button(window, text="Abort shutdown", command=abort, height=2, width=20).pack(pady=15, padx=20, anchor="center")
    tk.Button(window, text="Exit", command=app.destroy, height=2, width=20).pack(pady=10, padx=20, anchor="center")
    tk.Button(window, text="Back", command=lambda: back(window, app), height=2, width=20).pack(pady=10, padx=20, anchor="center")

    center_window(window)

def back(window, app):
    window.destroy()
    app.deiconify()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))