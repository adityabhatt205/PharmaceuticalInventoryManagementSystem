# main.py

# import
import tkinter as gui
import mysql.connector as sql
import os
from others.SQLGen import *
from itemFile import *


# variables
mainMessage = "Welcome to the Pharmaceutical Inventory Management System!"
mainItem = "Item File"


# functions
def mainPage():
    global root
    root = gui.Tk()
    frm = gui.Frame(root)
    menu = gui.Menu(root)
    root.config(menu=menu)
    fileMenu = gui.Menu(menu)
    menu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label='New')
    fileMenu.add_command(label='Open...')
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=root.quit)
    helpMenu = gui.Menu(menu)
    menu.add_cascade(label='Help', menu=helpMenu)
    helpMenu.add_command(label='About')
    root.mainloop()
    frm.pack()
    gui.Label(frm, text=mainMessage).grid(column=0, row=0, columnspan=3)
    gui.Button(frm, text="Item", command=item).grid(column=0, row=1)
    gui.Button(frm, text="Firm", command=item).grid(column=1, row=1)
    gui.Button(frm, text="Kilo", command=item).grid(column=2, row=1)
    root.mainloop()


def item():
    global root
    root.destroy()
    root = gui.Tk()
    frm = gui.Frame(root)
    frm.pack()
    gui.Label(frm, text=mainItem, fg="white", bg="blue").grid(row=0, columnspan=3)
    root.mainloop()


def freshStarter():
    global root
    root.destroy()
    root = gui.Tk()
    frm = gui.Frame(root)
    frm.pack()
    root.mainloop()


# main
mainPage()