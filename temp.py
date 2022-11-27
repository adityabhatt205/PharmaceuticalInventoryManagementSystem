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


def invoicePage():
    global root
    root.destroy()
    root = gui.Tk()
    root.config(bg=gui_bgColor)
    root.title("Invoice Register")
    root.geometry(f"{1350}x{int(root.winfo_screenheight() / 2)}+"
                  f"{int((root.winfo_screenwidth() / 2) - 1350 / 2)}+{int(root.winfo_screenheight() / 4)}")
    root.resizable(False, False)
    insertFrame = gui.Frame(root, bg=gui_bgColor, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    insertFrame.pack()
    gui.Label(insertFrame, text="Invoice Register File", bg=gui_bgColor, fg=gui_fgColor).grid(
        column=0, row=0, columnspan=3)
    canvas = gui.Canvas(insertFrame, width="1330")
    canvas.grid(row=6, column=0, columnspan=4)
    scroll = gui.Scrollbar(insertFrame, orient=gui.VERTICAL, command=canvas.yview)
    scroll.grid(row=6, column=5)
    canvas.configure(yscrollcommand=scroll.set, bg=gui_bgColor)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    resultFrame = gui.Frame(canvas, bg=gui_bgColor, borderwidth=2)
    resultFrame.grid(row=1, column=0)

    # Return Button
    gui.Button(insertFrame, text="Return", bg=gui_bgColor2, fg=gui_fgColor2, command=item).grid(row=4,
                                                                                                column=0,
                                                                                                columnspan=2,
                                                                                                pady=5)

    canvas.create_window((0, 0), window=resultFrame, anchor="nw")
    root.mainloop()


invoicePage()
