# main.py

# import
import tkinter as gui
from tkinter import Frame, filedialog, ttk
import mysql.connector as sql
import os
from others.SQLGen import *
from others.authCheck import *
from itemFile import *
from peopleList import *
import Export_Item
from PIL import ImageTk, Image

# variables
mainMessage = "Welcome to the Pharmaceutical Inventory Management System!"
mainItem = "Item File"
gui_bgColor = '#262626'
gui_bgColor2 = '#202121'
gui_fgColor = '#7a95ff'  # #9999ff
gui_fgColor2 = '#99e9ff'
gui_FontStyle = "Palatino"
root = gui.Tk()
geometry = f"{int(root.winfo_screenwidth() / 2)}x{int(root.winfo_screenheight() / 2)}+" \
           f"{int(root.winfo_screenwidth() / 4)}+{int(root.winfo_screenheight() / 4)}"
incorrectAttempts = 0


# functions
def about():
    open(r"others\open.txt")


def clearFields(a):
    for i in a:
        if type(i) != gui.StringVar:
            i.delete(0, gui.END)


def getFields(a):
    l = []
    for i in a:
        if type(i) == gui.StringVar():
            l.append(i)
        l.append(i.get())
    return tuple(l)


def startPage():
    global root
    root.destroy()
    root = gui.Tk()
    root.geometry(f"1280x720+{int((root.winfo_screenwidth() / 2) - 640)}+{int((root.winfo_screenheight() / 2) - 360)}")
    root.resizable(False, False)
    root.config(bg=gui_bgColor)
    root.title("Start Page: Enter credentials to continue")

    imageFrame = gui.Frame(root, width=1280, height=720, borderwidth=0)
    imageFrame.grid(column=3, row=0)
    homeImage = ImageTk.PhotoImage(Image.open(r"C:\Users\adity\Desktop\pyProjectOnPyCharm\others\Assets\HomePic01.jpg"))
    gui.Label(image=homeImage, borderwidth=0).grid(row=0, column=0)

    authPage = gui.Toplevel()
    authPage.config(bg=gui_bgColor)
    authPage.geometry(
        f"370x130+{int((root.winfo_screenwidth() / 2) - 640)}+{int((root.winfo_screenheight() / 2) - 360)}")
    authPage.title("Log In")
    authFrame = gui.Frame(authPage, width=450, height=120, bg=gui_bgColor, borderwidth=0)
    authFrame.pack()
    gui.Label(authFrame, text="User ID", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=0,
                                                                                                  column=0,
                                                                                                  sticky="w")
    gui.Label(authFrame, text="Password", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=1,
                                                                                                   column=0,
                                                                                                   sticky="w")
    userID_val = gui.Entry(authFrame, bg=gui_bgColor2, fg=gui_fgColor2, width=30)
    userID_val.grid(row=0, column=1)
    userPass_val = gui.Entry(authFrame, show="*", bg=gui_bgColor2, fg=gui_fgColor2, width=30)
    userPass_val.grid(row=1, column=1)

    buttonList = [
        userID_val, userPass_val
    ]
    check = gui.Label(authFrame, text="", bg=gui_bgColor, fg="red")
    check.grid(row=4, columnspan=2)

    gui.Button(authFrame, text="Submit", bg=gui_bgColor2, width=25,
               command=lambda: (authPage.quit(), mainPage()) if authCheck(getFields(buttonList)) == True
               else print(getFields(buttonList)) if getFields(buttonList) == ('', '') else (incorrectCred(check, root)),
               fg=gui_fgColor2).grid(row=2, column=0, pady=2)
    gui.Button(authFrame, text="Clear Fields", width=25, command=lambda: clearFields(buttonList), bg=gui_bgColor2,
               fg=gui_fgColor2).grid(row=2, column=1, pady=2)
    gui.Button(authFrame, text="Clear Fields", width=25, command=lambda: clearFields(buttonList), bg=gui_bgColor2,
               fg=gui_fgColor2).grid(row=3, column=0, columnspan=2, pady=0)
    authPage.resizable(False, False)
    root.mainloop()
    authPage.mainloop()


def incorrectCred(check, page):
    global incorrectAttempts
    incorrectAttempts += 1
    check["text"] = f'Incorrect Credentials! {3 - incorrectAttempts} attempts left'
    if incorrectAttempts >= 3:
        page.destroy()
    return check, incorrectAttempts


def mainPage():
    global root
    root.destroy()
    root = gui.Tk()
    root.config(bg=gui_bgColor)
    root.geometry(geometry)
    frm = gui.Frame(root, bg=gui_bgColor)
    frm.grid(row=0, column=0)
    root.title("Main Page")

    # menu = gui.Menu(root, bg=gui_bgColor, fg=gui_fgColor)
    # root.config(menu=menu, bg=gui_bgColor)
    # fileMenu = gui.Menu(menu, bg=gui_bgColor, fg=gui_fgColor)
    # menu.add_cascade(label="File", menu=fileMenu)
    # fileMenu.add_command(label='New')
    # fileMenu.add_command(label='Open...')
    # fileMenu.add_separator()
    # fileMenu.add_command(label='Exit', command=root.quit)
    # helpMenu = gui.Menu(menu, bg=gui_bgColor, fg=gui_fgColor)
    # menu.add_cascade(label='Help', menu=helpMenu)
    # helpMenu.add_command(label='About', command=about)

    gui.Label(frm, text=mainMessage, bg=gui_bgColor, fg=gui_fgColor, font=(gui_FontStyle, 20)) \
        .grid(column=0, row=0, columnspan=3, sticky="s")

    gui.Button(frm, text="Item", command=item, bg=gui_bgColor2, fg=gui_fgColor2, width=20). \
        grid(column=0, row=1)
    gui.Button(frm, text="Firm", command=firm, bg=gui_bgColor2, fg=gui_fgColor2, width=20). \
        grid(column=1, row=1)
    gui.Button(frm, text="3", command=startPage, bg=gui_bgColor2, fg=gui_fgColor2, width=20). \
        grid(column=2, row=1)
    gui.Button(frm, text="4", command=firm, bg=gui_bgColor2, fg=gui_fgColor2, width=20). \
        grid(column=0, row=2)
    gui.Button(frm, text="5", command=firm, bg=gui_bgColor2, fg=gui_fgColor2, width=20). \
        grid(column=1, row=2)
    gui.Button(frm, text="Log Out", command=startPage, bg=gui_bgColor2, fg=gui_fgColor2, width=20). \
        grid(column=2, row=2)

    # noinspection PyTypeChecker
    root.resizable(0, 0)
    root.mainloop()


def item():
    global root
    root.destroy()
    root = gui.Tk()
    root.config(bg=gui_bgColor)
    root.title("Item")
    root.geometry(f"{int(root.winfo_screenwidth() / 2)}x{int(root.winfo_screenheight() / 2)}")
    frm = gui.Frame(root, bg=gui_bgColor, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    frm.pack()
    gui.Label(frm, text="Item File: Pick an option to continue", bg=gui_bgColor, fg=gui_fgColor).grid(column=0, row=0,
                                                                                                      columnspan=3)
    gui.Button(frm, text="Insert", command=insertItem, bg=gui_bgColor2, fg=gui_fgColor2).grid(column=0, row=1)
    gui.Button(frm, text="Search", command=searchItem, bg=gui_bgColor2, fg=gui_fgColor2).grid(column=1, row=1)
    gui.Button(frm, text="Modify", command=item, bg=gui_bgColor2, fg=gui_fgColor2).grid(column=2, row=1)
    gui.Button(frm, text="Return", command=mainPage, bg=gui_bgColor2, fg=gui_fgColor2).grid(column=1, row=3)
    root.mainloop()


def insertItem():
    global root
    root.destroy()
    root = gui.Tk()
    root.title("Item: Adding New Records")
    root.config(bg=gui_bgColor)
    # root.geometry(geometry)
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
    itemCategory_val_d = gui.StringVar()
    itemCategory_val_dropdown = gui.OptionMenu(rootFrame, itemCategory_val_d, "I", "C", "T")
    itemCategory_val_dropdown.config(bg=gui_bgColor, fg=gui_fgColor, borderwidth=0, width=15)
    itemCategory_val_dropdown.grid(row=3, column=1, pady=5)
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
        itemID_val, itemName_val, itemCategory_val_d, company_val, composition_val, stockist_val, retailPrice_val,
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


def searchItemOutput(criteria, value, frame):
    for oldResults in frame.winfo_children():
        oldResults.destroy()
    data = itemSearch(criteria=criteria.get(), value=getFields([value])[0])
    frame.config(bg=gui_bgColor)
    k = 0
    width_list = [
        3, 25, 2, 25, 50, 15, 15, 15, 15, 10, 20, 20,
    ]
    orientation_list = [
        "right", "left", "left", "left", "left", "right", "right", "right", "right", "right", "right", "right"
    ]
    for i in range(len(data)):
        for j in range(len(data[i])):
            e = gui.Entry(frame)
            e.config(bg=gui_bgColor2, fg=gui_fgColor2, width=width_list[j], justify=orientation_list[j])
            e.grid(row=i, column=j, sticky="w")
            e.insert(k, data[i][j])
            k += 1


def searchItem():
    global root
    root.destroy()
    root = gui.Tk()
    root.title("Item: Searching Records")
    root.config(bg=gui_bgColor)
    root.geometry(f"{1350}x{int(root.winfo_screenheight() / 2)}+"
                  f"{int((root.winfo_screenwidth() / 2) - 1350 / 2)}+{int(root.winfo_screenheight() / 4)}")
    root.resizable(False, False)
    rootFrame = gui.Frame(root, bg=gui_bgColor, borderwidth=2)
    rootFrame.grid(row=0, column=0)
    gui.Label(rootFrame, text="Search Records", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=3,
                                                                                                         padx=100)
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
    resultFrame = gui.Frame(root, bg=gui_bgColor, borderwidth=2)
    resultFrame.grid(row=1, column=0)
    searchItemOutput(criteria=itemCriteria, value=searchValue, frame=resultFrame)

    # result = gui.Label(resultFrame, text=str(searchItemOutput(criteria=itemCriteria, value=searchValue,
    #                                                           frame=resultFrame)), bg=gui_bgColor, fg=gui_fgColor)
    # result.grid(row=5, column=0, pady=2, columnspan=3)

    # Search Button
    gui.Button(rootFrame, text="Search Item", bg=gui_bgColor2, fg=gui_fgColor2,
               command=lambda: searchItemOutput(criteria=itemCriteria, value=searchValue,
                                                frame=resultFrame)).grid(row=3, column=0, pady=2)
    # Clear Button
    gui.Button(rootFrame, text="Clear Fields", command=lambda: clearFields([searchValue]), bg=gui_bgColor2,
               fg=gui_fgColor2).grid(row=3, column=1, pady=2)
    # Return Button
    gui.Button(rootFrame, text="Return", bg=gui_bgColor2, fg=gui_fgColor2, command=item).grid(row=4,
                                                                                              column=0,
                                                                                              columnspan=2,
                                                                                              pady=5)
    root.mainloop()


def deleteItem():
    global root
    root.destroy()
    root = gui.Tk()
    root.title("Item: Deleting Records")
    root.config(bg=gui_bgColor)
    root.geometry(f"{1350}x{int(root.winfo_screenheight() / 2)}+"
                  f"{int((root.winfo_screenwidth() / 2) - 1350 / 2)}+{int(root.winfo_screenheight() / 4)}")
    root.resizable(False, False)
    rootFrame = gui.Frame(root, bg=gui_bgColor, borderwidth=2)
    rootFrame.grid(row=0, column=0)
    gui.Label(rootFrame, text="Search Records", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=3,
                                                                                                         padx=100)
    gui.Label(rootFrame, text="Field To Search", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=1,
                                                                                                          column=0,
                                                                                                          sticky="w")
    gui.Label(rootFrame, text="Value To Search", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=2,
                                                                                                          column=0,
                                                                                                          sticky="w")
    itemCriteria = gui.StringVar()
    itemCriteria.set("itemID")
    op = gui.OptionMenu(rootFrame, itemCriteria, "itemID", "itemName", "itemCategory", "company", "composition",
                        "packing", "batchNo", "expiryDate", "manufacturingDate")
    op.config(width=15, height=1, bg=gui_bgColor, fg=gui_fgColor, borderwidth=0)
    op.grid(row=1, column=1, sticky="e")
    searchValue = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2, width=21)
    searchValue.grid(row=2, column=1, sticky="e")
    # Result
    resultFrame = gui.Frame(root, bg=gui_bgColor, borderwidth=2)
    resultFrame.grid(row=1, column=0)

    # Search Button
    gui.Button(rootFrame, text="Search Item", bg=gui_bgColor2, fg=gui_fgColor2,
               command=lambda: searchItemOutput(criteria=itemCriteria, value=searchValue,
                                                frame=resultFrame)).grid(row=3, column=0, pady=2)
    # Clear Button
    gui.Button(rootFrame, text="Clear Fields", command=lambda: clearFields([searchValue]), bg=gui_bgColor2,
               fg=gui_fgColor2).grid(row=3, column=1, pady=2)
    # Return Button
    gui.Button(rootFrame, text="Return", bg=gui_bgColor2, fg=gui_fgColor2, command=item).grid(row=4,
                                                                                              column=0,
                                                                                              columnspan=2,
                                                                                              pady=5)
    root.mainloop()


def freshStarter():
    global root
    root.destroy()
    root = gui.Tk()
    frm = gui.Frame(root)
    frm.pack()
    root.mainloop()


def firm():
    global root
    root.destroy()
    root = gui.Tk()
    root.config(bg=gui_bgColor)
    root.title("Firm")
    root.geometry(f"{int(root.winfo_screenwidth() / 2)}x{int(root.winfo_screenheight() / 2)}")
    frm = gui.Frame(root, bg=gui_bgColor, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    frm.pack()
    gui.Label(frm, text="Firm File: Pick an option to continue", bg=gui_bgColor, fg=gui_fgColor).grid(column=0, row=0,
                                                                                                      columnspan=3)
    gui.Button(frm, text="Insert", command=insertFirm, bg=gui_bgColor2, fg=gui_fgColor2).grid(column=0, row=1)
    gui.Button(frm, text="Search", command=searchFirm, bg=gui_bgColor2, fg=gui_fgColor2).grid(column=1, row=1)
    gui.Button(frm, text="Modify", command="", bg=gui_bgColor2, fg=gui_fgColor2).grid(column=2, row=1)
    gui.Button(frm, text="Return", command=mainPage, bg=gui_bgColor2, fg=gui_fgColor2).grid(column=1, row=3)
    root.mainloop()


# noinspection PyTypeChecker
def insertFirm():
    global root
    root.destroy()
    root = gui.Tk()
    root.title("People: Adding New Records")
    root.config(bg=gui_bgColor)
    # root.geometry(geometry)
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
    pID_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    pID_val.grid(row=1, column=1, pady=5)
    pName_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    pName_val.grid(row=2, column=1, pady=5)
    pCategory_val_d = gui.StringVar()
    pCategory_val_d.set("C")
    pCategory_val_dropdown = gui.OptionMenu(rootFrame, pCategory_val_d, "S", "C")
    pCategory_val_dropdown.config(bg=gui_bgColor2, fg=gui_fgColor2, borderwidth=0, width=15)
    pCategory_val_dropdown.grid(row=3, column=1, pady=5)
    contactPerson_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    contactPerson_val.grid(row=4, column=1, pady=5)
    pAddress_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    pAddress_val.grid(row=5, column=1, pady=5)
    pCity_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    pCity_val.grid(row=6, column=1, pady=5)
    pinCode_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    pinCode_val.grid(row=7, column=1, pady=5)
    proprietor_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    proprietor_val.grid(row=8, column=1, pady=5)
    phoneNo_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    phoneNo_val.grid(row=9, column=1, pady=5)
    mobileNo_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    mobileNo_val.grid(row=10, column=1, pady=5)
    gstNo_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    gstNo_val.grid(row=11, column=1, pady=5)
    dlNo_val = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2)
    dlNo_val.grid(row=12, column=1, pady=5)
    buttonList = (
        pID_val, pName_val, pCategory_val_d, contactPerson_val, pAddress_val, pCity_val, pinCode_val,
        proprietor_val, phoneNo_val, mobileNo_val, gstNo_val, dlNo_val)
    gui.Button(rootFrame, text="Add People",
               command=lambda: (peopleAdder(getFields(buttonList)), clearFields(buttonList)),
               bg=gui_bgColor2, fg=gui_fgColor2) \
        .grid(row=14, column=0, pady=2)
    gui.Button(rootFrame, text="Clear Fields", command=lambda: clearFields(buttonList), bg=gui_bgColor2,
               fg=gui_fgColor2) \
        .grid(row=14, column=1, pady=2)
    gui.Button(rootFrame, text="Return", bg=gui_bgColor2, fg=gui_fgColor2, command=mainPage).grid(row=15,
                                                                                                  column=0,
                                                                                                  columnspan=2,
                                                                                                  pady=5)
    root.resizable(0, 0)
    root.mainloop()


def searchFirmOutput(criteria, value, frame):
    for oldResults in frame.winfo_children():
        oldResults.destroy()
    data = firmSearch(criteria=criteria.get(), value=getFields([value])[0])
    frame.config(bg=gui_bgColor)
    k = 0
    width_list = [
        3, 30, 2, 15, 30, 15, 10, 15, 15, 15, 20, 20,
    ]
    orientation_list = [
        "right", "left", "left", "left", "left", "right", "right", "right", "right", "right", "right", "right"
    ]
    for i in range(len(data)):
        for j in range(len(data[i])):
            e = gui.Entry(frame)
            e.config(bg=gui_bgColor2, fg=gui_fgColor2, width=width_list[j], justify=orientation_list[j])
            e.grid(row=i, column=j, sticky="w")
            e.insert(k, data[i][j])
            k += 1


def searchFirm():
    global root
    root.destroy()
    root = gui.Tk()
    root.title("Firm: Searching Records")
    root.config(bg=gui_bgColor)
    root.geometry(f"{1350}x{int(root.winfo_screenheight() / 2)}+"
                  f"{int((root.winfo_screenwidth() / 2) - 1350 / 2)}+{int(root.winfo_screenheight() / 4)}")
    root.resizable(False, False)
    rootFrame = gui.Frame(root, bg=gui_bgColor, borderwidth=2)
    rootFrame.grid(row=0, column=0)
    gui.Label(rootFrame, text="Search Records", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=3,
                                                                                                         padx=100)
    gui.Label(rootFrame, text="Field To Search", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=1,
                                                                                                          column=0,
                                                                                                          sticky="w")
    gui.Label(rootFrame, text="Value To Search", font=gui_FontStyle, bg=gui_bgColor, fg=gui_fgColor).grid(row=2,
                                                                                                          column=0,
                                                                                                          sticky="w")
    itemCriteria = gui.StringVar()
    itemCriteria.set("FirmID")
    op = gui.OptionMenu(rootFrame, itemCriteria, "FirmID", "SCName", "SCCategory", "contactPerson", "address",
                        "city", "pinCode", "proprietor", "phoneNo", "mobileNo", "gstN", "dlNo")
    op.config(width=15, height=1, bg=gui_bgColor, fg=gui_fgColor, borderwidth=0)
    op.grid(row=1, column=1, sticky="e")
    searchValue = gui.Entry(rootFrame, bg=gui_bgColor2, fg=gui_fgColor2, width=21)
    searchValue.grid(row=2, column=1, sticky="e")

    # Result
    resultFrame = gui.Frame(root, bg=gui_bgColor, borderwidth=2)
    resultFrame.grid(row=1, column=0)
    searchFirmOutput(criteria=itemCriteria, value=searchValue, frame=resultFrame)

    # Search Button
    gui.Button(rootFrame, text="Search Item", bg=gui_bgColor2, fg=gui_fgColor2,
               command=lambda: searchFirmOutput(criteria=itemCriteria, value=searchValue,
                                                frame=resultFrame)).grid(row=3, column=0, pady=2)
    # Clear Button
    gui.Button(rootFrame, text="Clear Fields", command=lambda: clearFields([searchValue]), bg=gui_bgColor2,
               fg=gui_fgColor2).grid(row=3, column=1, pady=2)
    # Return Button
    gui.Button(rootFrame, text="Return", bg=gui_bgColor2, fg=gui_fgColor2, command=item).grid(row=4,
                                                                                              column=0,
                                                                                              columnspan=2,
                                                                                              pady=5)
    root.mainloop()


# main
mainPage()
