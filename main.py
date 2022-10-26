# main.py

# import
import tkinter as gui
import mysql.connector as sql
import os
from others.SQLGen import *
from itemFile import *
from peopleList import *

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


def insertItem():
    root = gui.Tk()
    root.title("Item: Adding New Records")
    root.geometry("400x600")
    gui.Label(root, text="Add New Item", font="Cambria").grid(row=0, column=0, columnspan=2, padx=100)
    gui.Label(root, text="Item ID", font="Georgia").grid(row=1, column=0, sticky="w")
    gui.Label(root, text="Item Name", font="Georgia").grid(row=2, column=0, sticky="w")
    gui.Label(root, text="Item Category", font="Georgia").grid(row=3, column=0, sticky="w")
    gui.Label(root, text="Company", font="Georgia").grid(row=4, column=0, sticky="w")
    gui.Label(root, text="Composition", font="Georgia").grid(row=5, column=0, sticky="w")
    gui.Label(root, text="Rate", font="Georgia").grid(row=6, column=0, sticky="w")
    gui.Label(root, text="Stockist", font="Georgia").grid(row=7, column=0, sticky="w")
    gui.Label(root, text="Retail Price", font="Georgia").grid(row=8, column=0, sticky="w")
    gui.Label(root, text="MRP", font="Georgia").grid(row=9, column=0, sticky="w")
    gui.Label(root, text="Packing", font="Georgia").grid(row=10, column=0, sticky="w")
    gui.Label(root, text="Batch No.", font="Georgia").grid(row=11, column=0, sticky="w")
    gui.Label(root, text="Expiry Date", font="Georgia").grid(row=12, column=0, sticky="w")
    gui.Label(root, text="Manufacturing Date", font="Georgia").grid(row=13, column=0, sticky="w")
    itemID_val = gui.Entry(root)
    itemID_val.grid(row=1, column=1, pady=5)
    itemName_val = gui.Entry(root)
    itemName_val.grid(row=2, column=1, pady=5)
    itemCategory_val = gui.Entry(root)
    itemCategory_val.grid(row=3, column=1, pady=5)
    company_val = gui.Entry(root)
    company_val.grid(row=4, column=1, pady=5)
    composition_val = gui.Entry(root)
    composition_val.grid(row=5, column=1, pady=5)
    rate_val = gui.Entry(root)
    rate_val.grid(row=6, column=1, pady=5)
    retailPrice_val = gui.Entry(root)
    retailPrice_val.grid(row=7, column=1, pady=5)
    MRP_val = gui.Entry(root)
    MRP_val.grid(row=8, column=1, pady=5)
    packing_val = gui.Entry(root)
    packing_val.grid(row=9, column=1, pady=5)
    batchNo_val = gui.Entry(root)
    batchNo_val.grid(row=10, column=1, pady=5)
    expiryDate_val = gui.Entry(root)
    expiryDate_val.grid(row=11, column=1, pady=5)
    manufacturingDate_val = gui.Entry(root)
    manufacturingDate_val.grid(row=12, column=1, pady=5)
    entries = (
        int(itemID_val.get()),
        str(itemName_val.get()),
        str(itemCategory_val.get()),
        str(company_val.get()),
        str(composition_val.get()),
        int(rate_val.get()),
        int(retailPrice_val.get()),
        int(MRP_val.get()),
        int(packing_val.get()),
        int(batchNo_val.get()),
        int(expiryDate_val.get()),
        str(manufacturingDate_val.get())
    )
    gui.Button(root, text="Add Item", command=lambda: itemAdder(entries)).grid(row=14, column=0, pady=15)
    gui.Button(root, text="Clear Fields").grid(row=14, column=1, pady=15)
    gui.Button(root, text="someThing")
    root.mainloop()


# main
insertItem()
