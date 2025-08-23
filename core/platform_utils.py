from tkinter import messagebox
from core.commands import current_os

def ensure_os(target_os):
    return current_os() == target_os

def show_worng_os_error():
    messagebox.showerror("Error", "Wrong Operating System selected!")