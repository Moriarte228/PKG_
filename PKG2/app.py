import os
import pandas as pd
from tkinter import *
from tkinter import filedialog
from PIL import Image
import tkinter.ttk as ttk


win = Tk()
win.title('Image info')
win.geometry('500x500')
win.resizable(width=False, height=False)

def find_images_in_directory(directory_path):
    image_info_list = []

    for root, _, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.pcx')):
                img = Image.open(file_path)

                image_name = filename
                image_size = img.size
                image_dpi = img.info.get('dpi')
                image_mode = img.mode
                image_compression = img.info.get('compression')

                image_info_list.append({
                    'Image name': image_name,
                    'Image size (px)': image_size,
                    'Resolution (dpi)': image_dpi,
                    'Depth of color': image_mode,
                    'Compression': image_compression
                })

    return image_info_list
def dict_ask():
    global folder_path
    global image_info_list
    folder_path = filedialog.askdirectory()
    image_info_list = find_images_in_directory(folder_path)
    df = pd.DataFrame(image_info_list)
    show_table(df)


Label(text="Жмякнете на кнопку, чтобы получить информацию о файлах в папке").pack();
Button(text= "Choose the folder", width= 100, height=50, command=dict_ask).pack()

def show_table(df):
    w2 = Tk()
    w2.title('Информация о файлах в папках')
    w2.geometry('1200x600')
    table = ttk.Treeview(w2,
                         columns=['Image name', 'Image size (px)', 'Resolution (dpi)', 'Depth of color', 'Compression'], height=300)
    table.heading('#1', text='Image name')
    table.heading('#2', text='Image size (px)')
    table.heading('#3', text='Resolution (dpi)')
    table.heading('#4', text='Depth of color')
    table.heading('#5', text='Compression')
    table.column('#1', width=200, stretch=False)
    table.column('#2', width=200, stretch=False)
    table.column('#3', width=200, stretch=False)
    table.column('#4', width=200, stretch=False)
    table.column('#5', width=200, stretch=False)
    for index, row in df.iterrows():
        values = row.tolist()
        table.insert('', 'end', values=values)

    table.pack()
    w2.mainloop()

folder_path = ''
image_info_list = []

win.mainloop()