# main.py

# import
import tkinter as gui
from tkinter import Frame, filedialog, ttk
# import mysql.connector as sql
# import os
from others.SQLGen import *
from itemFile import *
from peopleList import *
import Export_Item

# variables
mainMessage = "Welcome to the Pharmaceutical Inventory Management System!"
mainItem = "Item File"
gui_bgColor = '#262626'
gui_fgColor = '#9999ff'
gui_FontStyle = "Palatino"

root = gui.Tk()


# functions
def about():
    open(r"others\open.txt")


def mainPage():
    global root
    root.destroy()
    root = gui.Tk()
    frm = gui.Frame(root, bg=gui_bgColor)
    frm.grid(row=0, column=0)
    menu = gui.Menu(root, bg=gui_bgColor, fg=gui_fgColor)
    root.config(menu=menu)
    fileMenu = gui.Menu(menu, bg=gui_bgColor, fg=gui_fgColor)
    menu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label='New')
    fileMenu.add_command(label='Open...')
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=root.quit)
    helpMenu = gui.Menu(menu, bg=gui_bgColor, fg=gui_fgColor)
    menu.add_cascade(label='Help', menu=helpMenu)
    helpMenu.add_command(label='About', command=about)
    gui.Label(frm, text=mainMessage, bg=gui_bgColor, fg=gui_fgColor).grid(column=0, row=0, columnspan=3)
    gui.Button(frm, text="Item", command=insertItem, bg=gui_bgColor, fg=gui_fgColor).grid(column=0, row=1)
    gui.Button(frm, text="Firm", command=peopleAdder, bg=gui_bgColor, fg=gui_fgColor).grid(column=1, row=1)
    gui.Button(frm, text="3rd option", command=item, bg=gui_bgColor, fg=gui_fgColor).grid(column=2, row=1)
    # noinspection PyTypeChecker
    root.resizable(0, 0)
    root.mainloop()


def item():
    global root
    root.destroy()
    root = gui.Tk()
    frm = gui.Frame(root)
    frm.pack()
    gui.Label(frm, text=mainItem, fg=gui_fgColor, bg=gui_bgColor).grid(row=0, column=0, columnspan=3)
    root.mainloop()


def freshStarter():
    global root
    root.destroy()
    root = gui.Tk()
    frm = gui.Frame(root)
    frm.pack()
    root.mainloop()


def clearFields(a):
    for i in a:
        i.delete(0, gui.END)


def getFields(a):
    l = []
    for i in a:
        l.append(i.get())
    return tuple(l)


def insertItem():
    global root
    root.destroy()
    root = gui.Tk()
    root.title("Item: Adding New Records")
    root.geometry("295x435")
    rootFrame = gui.Frame(root, bg=gui_bgColor)
    rootFrame.grid(row=0, column=0)
    gui.Label(rootFrame, text="Add New Item", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=0, column=0,
                                                                                                       columnspan=2,
                                                                                                       padx=100)
    gui.Label(rootFrame, text="Item ID", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=1, column=0,
                                                                                                  sticky="w")
    gui.Label(rootFrame, text="Item Name", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=2, column=0,
                                                                                                    sticky="w")
    gui.Label(rootFrame, text="Item Category", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=3, column=0,
                                                                                                        sticky="w")
    gui.Label(rootFrame, text="Company", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=4, column=0,
                                                                                                  sticky="w")
    gui.Label(rootFrame, text="Composition", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=5, column=0,
                                                                                                      sticky="w")
    gui.Label(rootFrame, text="Stockist", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=6, column=0,
                                                                                                   sticky="w")
    gui.Label(rootFrame, text="Retail Price", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=7, column=0,
                                                                                                       sticky="w")
    gui.Label(rootFrame, text="MRP", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=8, column=0,
                                                                                              sticky="w")
    gui.Label(rootFrame, text="Packing", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=9, column=0,
                                                                                                  sticky="w")
    gui.Label(rootFrame, text="Batch No.", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=10, column=0,
                                                                                                    sticky="w")
    gui.Label(rootFrame, text="Expiry Date", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=11, column=0,
                                                                                                      sticky="w")
    gui.Label(rootFrame, text="Manufacturing Date", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=12,
                                                                                                             column=0,
                                                                                                             sticky="w")
    itemID_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    itemID_val.grid(row=1, column=1, pady=5)
    itemName_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    itemName_val.grid(row=2, column=1, pady=5)
    itemCategory_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    itemCategory_val.grid(row=3, column=1, pady=5)
    company_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    company_val.grid(row=4, column=1, pady=5)
    composition_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    composition_val.grid(row=5, column=1, pady=5)
    stockist_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    stockist_val.grid(row=6, column=1, pady=5)
    retailPrice_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    retailPrice_val.grid(row=7, column=1, pady=5)
    MRP_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    MRP_val.grid(row=8, column=1, pady=5)
    packing_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    packing_val.grid(row=9, column=1, pady=5)
    batchNo_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    batchNo_val.grid(row=10, column=1, pady=5)
    expiryDate_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    expiryDate_val.grid(row=11, column=1, pady=5)
    manufacturingDate_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    manufacturingDate_val.grid(row=12, column=1, pady=5)
    buttonList = (
        itemID_val, itemName_val, itemCategory_val, company_val, composition_val, stockist_val, retailPrice_val,
        MRP_val,
        packing_val, batchNo_val, expiryDate_val, manufacturingDate_val)
    gui.Button(rootFrame, text="Add Item", command=lambda: (itemAdder(getFields(buttonList)), clearFields(buttonList)),
               bg=gui_bgColor, fg=gui_fgColor).grid(
        row=14, column=0, pady=2)
    gui.Button(rootFrame, text="Clear Fields", command=lambda: clearFields(buttonList), bg=gui_bgColor,
               fg=gui_fgColor).grid(row=14, column=1, pady=2)
    gui.Button(rootFrame, text="Return", bg=gui_bgColor, fg=gui_fgColor, command=mainPage).grid(row=15,
                                                                                                column=0,
                                                                                                columnspan=2,
                                                                                                pady=5)
    # noinspection PyTypeChecker
    root.resizable(0, 0)
    root.mainloop()


def peopleAdder():
    global root
    root.destroy()
    root = gui.Tk()
    root.title("People: Adding New Records")
    root.geometry("295x435")
    rootFrame = gui.Frame(root, bg=gui_bgColor)
    rootFrame.grid(row=0, column=0)
    gui.Label(rootFrame, text="Add New People", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=2,
                                                                                                         padx=100)
    gui.Label(rootFrame, text="ID", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=1, column=0,
                                                                                             sticky="w")
    gui.Label(rootFrame, text="Name", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=2, column=0,
                                                                                               sticky="w")
    gui.Label(rootFrame, text="Category", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=3, column=0,
                                                                                                   sticky="w")
    gui.Label(rootFrame, text="Contact Person", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=4,
                                                                                                         column=0,
                                                                                                         sticky="w")
    gui.Label(rootFrame, text="Address", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=5, column=0,
                                                                                                  sticky="w")
    gui.Label(rootFrame, text="City", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=6, column=0,
                                                                                               sticky="w")
    gui.Label(rootFrame, text="PIN Code", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=7, column=0,
                                                                                                   sticky="w")
    gui.Label(rootFrame, text="Proprietor", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=8, column=0,
                                                                                                     sticky="w")
    gui.Label(rootFrame, text="Phone No", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=9, column=0,
                                                                                                   sticky="w")
    gui.Label(rootFrame, text="Mobile No", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=10, column=0,
                                                                                                    sticky="w")
    gui.Label(rootFrame, text="GST No", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=11, column=0,
                                                                                                 sticky="w")
    gui.Label(rootFrame, text="DL No", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=12,
                                                                                                column=0,
                                                                                                sticky="w")
    pID_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    pID_val.grid(row=1, column=1, pady=5)
    pName_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    pName_val.grid(row=2, column=1, pady=5)
    pCategory_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    pCategory_val.grid(row=3, column=1, pady=5)
    contactPerson_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    contactPerson_val.grid(row=4, column=1, pady=5)
    pAddress_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    pAddress_val.grid(row=5, column=1, pady=5)
    pCity_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    pCity_val.grid(row=6, column=1, pady=5)
    pinCode_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    pinCode_val.grid(row=7, column=1, pady=5)
    proprietor_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    proprietor_val.grid(row=8, column=1, pady=5)
    phoneNo_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    phoneNo_val.grid(row=9, column=1, pady=5)
    mobileNo_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    mobileNo_val.grid(row=10, column=1, pady=5)
    gstNo_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    gstNo_val.grid(row=11, column=1, pady=5)
    dlNo_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    dlNo_val.grid(row=12, column=1, pady=5)
    buttonList = (
        pID_val, pName_val, pCategory_val, contactPerson_val, pAddress_val, pCity_val, pinCode_val,
        proprietor_val,
        phoneNo_val, mobileNo_val, gstNo_val, dlNo_val)
    gui.Button(rootFrame, text="Add People", command=lambda: (peopleAdder(buttonList), clearFields(buttonList)),
               bg=gui_bgColor, fg=gui_fgColor).grid(
        row=14, column=0, pady=2)
    gui.Button(rootFrame, text="Clear Fields", command=lambda: clearFields(buttonList), bg=gui_bgColor,
               fg=gui_fgColor).grid(row=14, column=1, pady=2)
    gui.Button(rootFrame, text="Return", bg=gui_bgColor, fg=gui_fgColor, command=mainPage).grid(row=15,
                                                                                                column=0,
                                                                                                columnspan=2,
                                                                                                pady=5)
    # noinspection PyTypeChecker
    root.resizable(0, 0)
    root.mainloop()


# main
mainPage()
