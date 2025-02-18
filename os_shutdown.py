import os
import platform
import tkinter as tk
from tkinter import messagebox

def shutdown():
    current_os = platform.system()

    timer = timer_entry.get()
    try:
        timer = int(timer)
        if messagebox.askokcancel("Shutdown", "Do you really want to shut down the computer?"):     #ask the user if he wants to shutdown the os, you can take out the first 'if' statement if you dont want a checkbox asking if you really want to shutdown your computer and if you take out the first 'if' statement then you can take out the else statement too.
            if current_os == "Windows":
                os.system(f"shutdown /s /t {timer}")    #/s gives the os the command that it wants to shutdown, /t is time in seconds
            else:
                messagebox.showerror("Error", "Unsupported OS")
    except ValueError:
        messagebox.showerror("Invalid number", "Enter valid number")
#Main window
app = tk.Tk() #declaring the main window
app.title("Shutdown GUI")

#label
label = tk.label(app, text="Enter time in seconds:")
label.pack(pady=10)

#entry
timer_entry = tk.Entry(app, width=10)
timer_entry.pack(pady=5)

#button
shutdown_button = tk.Button(app, text="Shutdown", command=shutdown, height=2, width=10) #this creates the button, the 'app' is the parent or master class that gets called, the rest is self explanatory
shutdown_button.pack(pady=20)

app.mainloop()
#You can use this little script for those nights where you start a video or a movie and you know you will definitely fall asleep and you want to save some money on your energy bill.