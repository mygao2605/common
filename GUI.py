import tkinter as tk
from tkinter import filedialog
import os
import subprocess

def on_button_click():
    global file_path  # Declare file_path as global to access it in run()
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        if os.name == 'nt':
            os.startfile(file_path)
        elif os.name == 'posix' and 'darwin' in os.uname().sysname.lower():
            subprocess.call(['open', file_path])
        elif os.name == 'posix':
            subprocess.call(['xdg-open', file_path])
    inputtxt.delete("1.0", "end")  # Clear any existing text in the Text widget
    inputtxt.insert("1.0", file_path)  

def sel():
    selection = f"You selected the option {var.get()}"
def run():
    # This function now uses global variables
    print(f"Selected file path: {file_path}")
    print(f"Selected option: {var.get()}")

root = tk.Tk()
root.title("COMMON")
root.geometry("300x250")  # Adjusted size to accommodate button text

label = tk.Label(root, text="COMMON APP")
label.pack(pady=20)
inputtxt = tk.Text(root, height =1, width = 30)
inputtxt.pack()


button = tk.Button(root, text="Choose the file (.xlsx)", command=on_button_click)
button.pack(pady=20)

var = tk.StringVar()  # Use StringVar to match Radiobutton values
radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

R1 = tk.Radiobutton(radio_frame, text="HAN", variable=var, value="HAN", command=sel)
R1.pack(side=tk.LEFT, padx=5)

R2 = tk.Radiobutton(radio_frame, text="DMP", variable=var, value="DMP", command=sel)
R2.pack(side=tk.LEFT, padx=5)

# Declare file_path globally so it can be used in the run function
file_path = ""

button_run = tk.Button(root, text="Run", command=run)
button_run.pack(pady=20)

root.mainloop()
