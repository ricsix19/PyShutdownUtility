import os
import platform
import tkinter as tk
from tkinter import messagebox

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
def abort_shutdown():
    current_os = platform.system()
    if messagebox.askokcancel("Abort shut down", "Do you really want to abort shutting down the computer?"):
        if current_os == "Windows":
            os.system("shutdown /a")
        if current_os == "Linux":
            os.system("sudo shutdown -c")
    else:
        messagebox.showerror("Error", "Unsupported OS")

def exitButton():
    if messagebox.askokcancel("Exit", "Do you really want to exit the application?"):
        app.destroy()

def on_closing(window):
     window.destroy()
     app.deiconify()

def windows_Display():
    app.withdraw()
    windows_window = tk.Toplevel(app)
    windows_window.title("Windows")

    windows_window.geometry("300x400")
    windows_window.resizable(False, False)

    windows_window.deiconify()

    label = tk.Label(windows_window, text="Enter shut down time in seconds:")
    label.pack(pady=10)

    timer_entry = tk.Entry(windows_window, width=50)
    timer_entry.pack(pady=10, padx=20)
    def windows_shutdown():
        timer = timer_entry.get()
        current_os = platform.system()

        try:
            timer = int(timer)
            if messagebox.askokcancel("Shutdown", "Do you really want to shut down the computer?"):
                if current_os == "Windows":
                    os.system(f"shutdown /s /t {timer}")  #/s gives the os the command that it wants to shut down, /t is time in seconds
                elif current_os != "Windows":
                    messagebox.showerror("Error", "Unsupported OS")
        except ValueError:
            messagebox.showerror("Invalid number", "Enter valid number")

    shutdown_button = tk.Button(windows_window, text="Shut down", command=windows_shutdown, height=2, width=20)
    shutdown_button.pack(pady=10, padx=20, anchor="center")

    abort_shutdown_button = tk.Button(windows_window, text="Abort shut down", command=abort_shutdown, height=2, width=20)
    abort_shutdown_button.pack(pady=15, padx=20, anchor="center")

    exit_button = tk.Button(windows_window, text="Exit", command=exitButton, height=2, width=20)
    exit_button.pack(pady=10, padx=20, anchor="center")

    back_button = tk.Button(windows_window, text="Back", command=lambda: on_closing(windows_window), height=2, width=20)
    back_button.pack(pady=10, padx=20, anchor="center")

    center_window(windows_window)

def linux_Display():
    app.withdraw()
    linux_window = tk.Toplevel(app)
    linux_window.title("Linux")

    linux_window.deiconify()

    label = tk.Label(linux_window, text="Enter shut down time:")
    label.pack(pady=10)

    timer_entry = tk.Entry(linux_window, width=50)
    timer_entry.pack(pady=10, padx=20)

    def linux_shutdown():
        linux_timer = timer_entry.get()
        current_os = platform.system()
        try:
            if messagebox.askokcancel("Shutdown", "Do you really want to shut down the computer?"):
                if current_os == "Linux":
                    os.system(f"sudo shutdown -h {linux_timer}")
                elif current_os != "Linux":
                    messagebox.showerror("Error", "Unsupported OS")
        except ValueError:
            messagebox.showerror("Invalid number", "Enter valid number")

    shutdown_button = tk.Button(linux_window, text="Shut down", command=linux_shutdown, height=2, width=20)
    shutdown_button.pack(pady=10, padx=20, anchor="center")

    abort_shutdown_button = tk.Button(linux_window, text="Abort shut down", command=abort_shutdown, height=2, width=20)
    abort_shutdown_button.pack(pady=15, padx=20, anchor="center")

    exit_button = tk.Button(linux_window, text="Exit", command=exitButton, height=2, width=20)
    exit_button.pack(pady=10, padx=20, anchor="center")

    back_button = tk.Button(linux_window, text="Back", command=lambda: on_closing(linux_window), height=2, width=20)
    back_button.pack(pady=10, padx=20, anchor="center")

#Main window
app = tk.Tk()
app.title("Shut down GUI")

label = tk.Label(app, text="Choose which operating system you use!")
label.pack(pady=10)

windows_button = tk.Button(app, text="Windows", command=windows_Display, height=2, width=20)
windows_button.pack(pady=10, padx=20, anchor="center")

linux_button = tk.Button(app, text="Linux", command=linux_Display, height=2, width=20)
linux_button.pack(pady=10, padx=20, anchor="center")

exit_button = tk.Button(app, text="Exit", command=exitButton, height=2, width=20)
exit_button.pack(pady=10, padx=20, anchor="center")

app.mainloop()