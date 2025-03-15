import os
import platform
import tkinter as tk
from tkinter import messagebox

def shutdown():
    current_os = platform.system()

    timer = timer_entry.get()
    try:
        timer = int(timer)
        if messagebox.askokcancel("Shutdown", "Do you really want to shut down the computer?"):
            if current_os == "Windows":
                os.system(f"shutdown /s /t {timer}")  #/s gives the os the command that it wants to shut down, /t is time in seconds
            if current_os == "Linux":
                linux_timer = timer_entry.get()
                # for security measures it stays with sudo, so no one can shut down your linux machine without your password
                os.system(f"sudo shutdown -h {linux_timer}")
            else:
                messagebox.showerror("Error", "Unsupported OS")
    except ValueError:
        messagebox.showerror("Invalid number", "Enter valid number")

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

#Main window
app = tk.Tk()
app.title("Shut down GUI")

#Main label
label = tk.Label(app, text="Enter time in seconds:")
label.pack(pady=10)

#Entry
timer_entry = tk.Entry(app, width=50)
timer_entry.pack(pady=10, padx=20)

#Shut down button
shutdown_button = tk.Button(app, text="Shut down", command=shutdown, height=2, width=20)
shutdown_button.pack(pady=10, padx=20, anchor="center")

#Button for aborting shut down
abort_shutdown_button = tk.Button(app, text="Abort shut down", command=abort_shutdown, height=2, width=20)
abort_shutdown_button.pack(pady=15, padx=20, anchor="center")

#Exit button
exit_button = tk.Button(app, text="Exit", command=exitButton, height=2, width=20)
exit_button.pack(pady=10, padx=20, anchor="center")
app.mainloop()