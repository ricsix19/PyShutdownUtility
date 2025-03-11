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
            else:
                messagebox.showerror("Error", "Unsupported OS")
    except ValueError:
        messagebox.showerror("Invalid number", "Enter valid number")

#Main window
app = tk.Tk()
app.title("Shutdown GUI")

#Label
label = tk.label(app, text="Enter time in seconds:")
label.pack(pady=10)

#Entry
timer_entry = tk.Entry(app, width=10)
timer_entry.pack(pady=5)

#Button
shutdown_button = tk.Button(app, text="Shutdown", command=shutdown, height=2, width=10)
shutdown_button.pack(pady=20)

app.mainloop()