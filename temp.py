from main import *

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


# noinspection PyGlobalUndefined
def insertPurReg():
    global root
    root.destroy()
    root = gui.Tk()
    root.title("Purchase Register: Adding New Records")
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
    gui.Label(rootFrame, text="PIN Code", font=gui_FontStyle, bg=gui_bgCol  or, fg=gui_fgColor).grid(row=7, column=0,
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
    root.resizable(False, False)
    root.mainloop()


insertPurReg()