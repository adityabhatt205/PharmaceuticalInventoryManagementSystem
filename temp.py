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


insertFirm()
