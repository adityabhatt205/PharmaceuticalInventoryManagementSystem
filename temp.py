# main.py

# import
import tkinter as gui
from tkinter import Frame, filedialog, ttk
import mysql.connector as sql
import os
from main import *
# from others.SQLGen import *
from others.authCheck import *
from files.itemFile import *
from files.SuppCust import *
# import Export_Item
import csv
from PIL import ImageTk, Image

# variables
mainMessage = "Welcome to the Pharmaceutical Inventory Management System!"
mainItem = "Item File"
gui_bgColor = '#000000'
gui_bgColor2 = '#020208'
gui_fgColor = '#ffffff'  # #9999ff
gui_fgColor2 = '#d9e3fa'
gui_FontStyle = "NotoSans"
root = gui.Tk()
geometry = f"{int(root.winfo_screenwidth())}x{int(root.winfo_screenheight())}+" \
           f"{int(root.winfo_screenwidth() / 4)}+{int(root.winfo_screenheight() / 4)}"
incorrectAttempts = 0


gui.Label(root, text="0, 0").grid(row=0, column=0)
gui.Label(root, text="1, 0").grid(row=1, column=0)
gui.Label(root, text="0, 1").grid(row=0, column=1)
gui.Label(root, text="1, 1").grid(row=1, column=1)
root.mainloop()