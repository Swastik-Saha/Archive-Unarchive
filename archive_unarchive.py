import shutil, os

import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename
import tkinter.messagebox as tmsg


rootmain = tk.Tk()
rootmain.title("Zip file manager")
canvas_width = 930
canvas_height = 245
rootmain.geometry(f"{canvas_width}x{canvas_height}")

root = tk.Canvas(rootmain, width=canvas_width, height=canvas_height)
root.pack()



# ====== Functions used in program ========

def choose_zip_dir():
    zip_path = askdirectory(title='Select the folder to be zipped')
    zip_dir.set(zip_path)
    zip_dir_entry.update()


def choose_unzip_dir():
    unzip_path = askopenfilename(title='Select ZIP File', filetypes=(('zip files', "*.zip"),))
    unzip_dir.set(unzip_path)
    unzip_dir_entry.update()


def unzip_file():
    input_file_path = unzip_dir.get()
    output_path = input_file_path.rstrip('.zip')
    shutil.unpack_archive(f'{input_file_path}', f'{output_path}')
    unzip_dir.set('')
    unzip_dir_entry.update()
    tmsg.showinfo('Unzipped', f'Your file is unzipped in\n{output_path}')


def zip_folder():
    input_path = zip_dir.get()
    output_file_path = input_path
    shutil.make_archive(f'{output_file_path}', 'zip', f'{input_path}')
    zip_dir.set('')
    zip_dir_entry.update()
    tmsg.showinfo('Zipped', f'Your folder is zipped at \n{input_path}')



zipy = 30
zipx = 60

unzipy = 30
unzipx = 550


zip_label = tk.Label(root, text='Choose the folder to ZIP', font='calibri 20 bold')
zip_label.place(x=zipx, y=zipy)

zip_dir = tk.StringVar()
zip_dir.set('')
zip_dir_entry = tk.Entry(root, text=zip_dir, font='calibri 15')
zip_dir_entry.place(x=zipx+10, y=zipy+60)

zip_dir_button = tk.Button(root, text='Choose Folder', font='calibri 10 bold', command=choose_zip_dir)
zip_dir_button.place(x=zipx+215, y=zipy+60)

unzip_ok_button = tk.Button(root, text='Ok', font='calibri 15 bold', padx=20, command=zip_folder)
unzip_ok_button.place(x=zipx+80, y=zipy+110)

line_x = canvas_width/2
root.create_line(line_x, 0, line_x, canvas_width, fill='black', width=5)

unzip_label = tk.Label(root, text='Choose the folder to UNZIP', font='calibri 20 bold')
unzip_label.place(x=unzipx, y=unzipy)

unzip_dir = tk.StringVar()
unzip_dir.set('')
unzip_dir_entry = tk.Entry(root, text=unzip_dir, font='calibri 15')
unzip_dir_entry.place(x=unzipx+10, y=unzipy+60)

unzip_dir_button = tk.Button(root, text='Choose File', font='calibri 10 bold', command=choose_unzip_dir)
unzip_dir_button.place(x=unzipx+215, y=unzipy+60)

unzip_ok_button = tk.Button(root, text='Ok', font='calibri 15 bold', padx=20, command=unzip_file)
unzip_ok_button.place(x=unzipx+80, y=unzipy+110)


rootmain.mainloop()
