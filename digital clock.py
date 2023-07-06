import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock)  # Update every second

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
label.pack(padx=20, pady=20)

update_clock()

root.mainloop()