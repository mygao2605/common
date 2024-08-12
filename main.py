# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import os
import shutil
import tkinter as tk
from tkinter import filedialog
import os
import subprocess
from pip._vendor.rich import print


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def open_excel_file(path, y):
    # file_path = '/Users/tunguyen/Desktop/vtx/DMVT.xlsx'
    # path.replace("\\", "/")
    print("--------")
    print(path)
    print(y)
    movies = pd.read_excel(path, y, dtype=str)
    movies_subset = movies[['STT', 'THÔNG SỐ', 'MÃ VẬT TƯ']]

    # print(movies_subset.values[0, 1])
    # print(movies_subset.count())
    split_path = os.path.split(path)

    base_path = split_path[0]
    root_path = base_path + '/Sort'
    # print(root_path)
    if not os.path.exists(root_path):
        os.mkdir(root_path)
    stt_spec = '0.0'
    name_sub = ""
    code_sub = ""

    for i in movies_subset.index:
        if movies_subset.values[i, 1] == movies_subset.values[i, 1] and movies_subset.values[i, 1] != '-':
            if movies_subset.values[i, 1] == 'HÀN':
                if stt_spec not in movies_subset.values[i, 0]:
                    stt_spec = movies_subset.values[i, 0].rstrip()
                    name_sub = movies.values[i, 2].rstrip()
                    code_sub = movies.values[i, 4].rstrip()
                    if not os.path.exists(root_path + '//' + 'HÀN_' + stt_spec + '_' + code_sub + '_' + name_sub):
                        os.mkdir(root_path + '//' + 'HÀN_' + stt_spec + '_' + code_sub + '_' + name_sub)
                    if not os.path.exists(root_path + '//' + 'HÀN_' + stt_spec + '_' + code_sub + '_' + name_sub + '//PDF'):
                        os.mkdir(root_path + '//' + 'HÀN_' + stt_spec + '_' + code_sub + '_' + name_sub + '//PDF')
                    if not os.path.exists(root_path + '//' + 'HÀN_' + stt_spec + '_' + code_sub + '_' + name_sub + '//DWG'):
                        os.mkdir(root_path + '//' + 'HÀN_' + stt_spec + '_' + code_sub + '_' + name_sub + '//DWG')
            else:
                if not os.path.exists(root_path + '//' + movies_subset.values[i, 1].rstrip()):
                    os.mkdir(root_path + '//' + movies_subset.values[i, 1].rstrip())
                    
                if not os.path.exists(root_path + '//' + movies_subset.values[i, 1].rstrip() + '//PDF'):
                    os.mkdir(root_path + '//' + movies_subset.values[i, 1].rstrip() + '//PDF')
                    
                if not os.path.exists(root_path + '//' + movies_subset.values[i, 1].rstrip() + '//DWG'):
                    os.mkdir(root_path + '//' + movies_subset.values[i, 1].rstrip() + '//DWG')
                    
            atoi = movies_subset.values[i, 0]
            pdf_file = find(movies_subset.values[i, 2] + '.pdf', base_path) 
            if pdf_file:
                path_file =root_path + '//' + movies_subset.values[i, 1].rstrip() + '//PDF' + '//' + movies_subset.values[i, 2] + '.pdf'
                if movies_subset.values[i, 1] != "HÀN":
                    if not os.path.exists(path_file):
                        shutil.copyfile(pdf_file, path_file) 
                if stt_spec in str(atoi):
                    shutil.copyfile(pdf_file,root_path + '//' + 'HÀN_' + stt_spec + '_' + code_sub + '_' + name_sub + '//PDF' + '//' + movies_subset.values[i, 2] + '.pdf')
        
            cad_file = find(movies_subset.values[i, 2] + '.dwg', base_path)
            if cad_file:
                path_file =root_path + '//' + movies_subset.values[i, 1].rstrip() + '//DWG' + '//' + movies_subset.values[i, 2] + '.dwg'
                if movies_subset.values[i, 1] != "HÀN":
                    if not os.path.exists(path_file):
                        shutil.copyfile(pdf_file, path_file) 
                if stt_spec in str(atoi):
                    shutil.copyfile(cad_file,root_path + '//' + 'HÀN_' + stt_spec + '_' + code_sub + '_' + name_sub + '//DWG' + '//' + movies_subset.values[i, 2] + '.dwg')

def on_button_click():
        global file_path  # Declare file_path as global to access it in run()
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        # if file_path:
        #     if os.name == 'nt':
        #         os.startfile(file_path)
        #     elif os.name == 'posix' and 'darwin' in os.uname().sysname.lower():
        #         subprocess.call(['open', file_path])
        #     elif os.name == 'posix':
        #         subprocess.call(['xdg-open', file_path])
        inputtxt.delete("1.0", "end")  # Clear any existing text in the Text widget
        inputtxt.insert("1.0", file_path)  

def sel():
    selection = f"You selected the option {var.get()}"
def run():
    # This function now uses global variables
    print(f"Selected file path: {file_path}")
    print(f"Selected option: {var.get()}")
    open_excel_file(file_path,var.get())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    

    root = tk.Tk()
    root.title("COMMON")
    root.geometry("350x300")  # Adjusted size to accommodate button text

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
    
    # print('Enter file path:')
    # x = input()
    # print('Choose the sheet:')
    # y = input()
    # # print('Hello, ' + x)
    # open_excel_file(x,y)
    # print('Done')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
