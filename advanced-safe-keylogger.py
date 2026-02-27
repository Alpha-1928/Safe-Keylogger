import tkinter as tk
from datetime import datetime

LOG_FILE = "advanced_keystrokes_log.txt"

def log_key(event):
    key = event.keysym
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} - {key}\n")

def clear_log():
    open(LOG_FILE, "w").close()
    status_label.config(text="Log file cleared!")

# Create main window
root = tk.Tk()
root.title("Safe Key Capture Project")
root.geometry("500x300")

instruction = tk.Label(root, text="Type inside this window. Keys will be logged safely.",
                       font=("Arial", 12))
instruction.pack(pady=10)

text_area = tk.Text(root, height=10)
text_area.pack(pady=10)

text_area.bind("<Key>", log_key)

clear_button = tk.Button(root, text="Clear Log File", command=clear_log)
clear_button.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
