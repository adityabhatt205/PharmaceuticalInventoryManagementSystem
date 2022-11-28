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
    # Defining the window
    global root
    root.destroy()
    root = gui.Tk()
    root.config(bg=gui_bgColor)
    root.title("Invoice Register")
    root.geometry(f"{1350}x{int(root.winfo_screenheight() / 2)}+"
                  f"{int((root.winfo_screenwidth() / 2) - 1350 / 2)}+{int(root.winfo_screenheight() / 4)}")
    root.resizable(False, False)

    # frame to enter invoice
    insertFrame = gui.Frame(root, bg=gui_bgColor, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    insertFrame.grid(row=0, column=1, pady=5)
    gui.Label(insertFrame, text="Invoice Register File", bg=gui_bgColor, fg=gui_fgColor).grid(
        column=0, row=0, columnspan=3)

    canvas = gui.Canvas(insertFrame, width="1030")
    canvas.grid(row=6, column=0, columnspan=4)
    scroll = gui.Scrollbar(insertFrame, orient=gui.VERTICAL, command=canvas.yview)
    scroll.grid(row=6, column=5)
    canvas.configure(yscrollcommand=scroll.set, bg=gui_bgColor)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # frame to insert inside canvas
    invoiceResultFrame = gui.Frame(canvas, bg=gui_bgColor, borderwidth=2)
    invoiceResultFrame.grid(row=1, column=0)

    canvas.create_window((0, 0), window=invoiceResultFrame, anchor="nw")

    # frame to enter entries for invoice
    rootFrame = gui.Frame(root, bg=gui_bgColor)
    rootFrame.grid(row=0, column=0)

    gui.Label(rootFrame, text="Add Items", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=0, column=0,
                                                                                                    columnspan=2,
                                                                                                    padx=100)
    gui.Label(rootFrame, text="Item ID", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=1, column=0,
                                                                                                  sticky="w")
    gui.Label(rootFrame, text="Customer ID", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=2, column=0,
                                                                                                      sticky="w")
    gui.Label(rootFrame, text="Mfg Date", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=3, column=0,
                                                                                                   sticky="w")
    gui.Label(rootFrame, text="Exp Date", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=4, column=0,
                                                                                                   sticky="w")
    gui.Label(rootFrame, text="Dis Percent", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=5, column=0,
                                                                                                      sticky="w")
    gui.Label(rootFrame, text="Qty", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=6, column=0,
                                                                                              sticky="w")

    # Entry Boxes
    itemID_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    itemID_val.grid(row=1, column=1, pady=5)
    custID_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    custID_val.grid(row=2, column=1, pady=5)
    mfdDate_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    mfdDate_val.grid(row=3, column=1, pady=5)
    expDate_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    expDate_val.grid(row=4, column=1, pady=5)
    discPer_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    discPer_val.grid(row=5, column=1, pady=5)
    qty_val = gui.Entry(rootFrame, bg=gui_bgColor, fg=gui_fgColor)
    qty_val.grid(row=6, column=1, pady=5)

    buttonList = [
        itemID_val, custID_val, mfdDate_val, expDate_val, discPer_val, qty_val
    ]

    gui.Button(rootFrame, text="Add Item",
               command=lambda: (invoiceItemOutput(list(getFields(buttonList)), invoiceResultFrame),
                                clearFields(buttonList)),
               bg=gui_bgColor, fg=gui_fgColor).grid(
        row=14, column=0, pady=2)
    gui.Button(rootFrame, text="Clear Fields", command=lambda: clearFields(buttonList), bg=gui_bgColor,
               fg=gui_fgColor).grid(row=14, column=1, pady=2)

    # frame to search itemID
    rootFrame = gui.Frame(root, bg=gui_bgColor, borderwidth=2, relief="sunken")
    rootFrame.grid(row=1, column=0, columnspan=3)

    gui.Label(rootFrame, text="Search Records", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=2,
                                                                                                         padx=0)
    gui.Label(rootFrame, text="Field To Search", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=1,
                                                                                                          column=0,
                                                                                                          sticky="w")
    gui.Label(rootFrame, text="Value To Search", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=2,
                                                                                                          column=0,
                                                                                                          sticky="w"
                                                                                                          )

    itemCriteria = gui.StringVar()
    itemCriteria.set("itemID")
    op = gui.OptionMenu(rootFrame, itemCriteria, "itemID", "itemName", "itemCategory", "company", "composition",
                        "packing", "batchNo", "expiryDate", "manufacturingDate")
    op.config(width=15, height=1, bg=gui_bgColor, fg=gui_fgColor, borderwidth=0)
    op.grid(row=1, column=1, sticky="e")

    searchValue = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2, width=21)
    searchValue.grid(row=2, column=1, sticky="e")

    # Result
    canvas = gui.Canvas(rootFrame, width="1330")
    canvas.grid(row=6, column=0, columnspan=4)
    scroll = gui.Scrollbar(rootFrame, orient=gui.VERTICAL, command=canvas.yview)
    scroll.grid(row=6, column=5)
    canvas.configure(yscrollcommand=scroll.set, bg=gui_bgColor)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    resultFrame = gui.Frame(canvas, bg=gui_bgColor, borderwidth=2)
    resultFrame.grid(row=1, column=0)

    searchItemOutput(criteria=itemCriteria, value=searchValue, frame=resultFrame)

    # Search Button
    gui.Button(rootFrame, text="Search Item", bg=gui_bgColor2, fg=gui_fgColor2,
               command=lambda: searchItemOutput(criteria=itemCriteria, value=searchValue,
                                                frame=resultFrame)).grid(row=3, column=0, pady=2)

    # Clear Button
    gui.Button(rootFrame, text="Clear Fields", command=lambda: clearFields([searchValue]), bg=gui_bgColor2,
               fg=gui_fgColor2).grid(row=3, column=1, pady=2)

    canvas.create_window((0, 0), window=resultFrame, anchor="nw")

    # submit invoice frame
    invoiceControlFrame = gui.Frame(rootFrame, bg=gui_bgColor, borderwidth=2, relief="sunken")
    invoiceControlFrame.grid(row=0, column=3, rowspan=3)
    gui.Button(invoiceControlFrame, text="Generate Invoice", bg=gui_bgColor2, fg=gui_fgColor2,
               command=lambda: searchItemOutput(criteria=itemCriteria, value=searchValue,
                                                frame=resultFrame)).grid(row=0, column=0, pady=2)

    # Clear Button
    gui.Button(invoiceControlFrame, text="Return", command=mainPage, bg=gui_bgColor2,
               fg=gui_fgColor2).grid(row=0, column=1, pady=2)

    # mainloop
    root.mainloop()


row = 0


def invoiceItemOutput(data, frame):
    global row
    frame.config(bg=gui_bgColor)
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    value = data[0]
    cur.execute(
        f"""
            SELECT * FROM item
            WHERE itemID = '{value}'
        """
    )
    results = cur.fetchall()
    cur.close()
    con.close()
    print(results)
    results = results[0]
    print(results)
    final_data = [row + 1, results[1], results[2], results[3], data[2], data[3], data[4], data[5],
                  float((1 - (float(data[4]) / 100))
                        * float(results[6])), float((1 - (float(data[4]) / 100)) * float(results[6])) * float(data[5])]

    k = 0
    width_list = [
        3, 30, 3, 30, 15, 15, 15, 15, 15, 15, 15, 15, 15
    ]
    orientation_list = [
        "right", "left", "left", "left", "left", "right", "right", "right", "right", "right", "right", "right"
    ]
    for i in range(len(final_data)):
        e = gui.Entry(frame)
        e.config(bg=gui_bgColor2, fg=gui_fgColor2, width=width_list[i], justify=orientation_list[i])
        e.grid(row=row, column=i, sticky="w")
        e.insert(k, final_data[i])
        k += 1
    row += 1


invoicePage()
