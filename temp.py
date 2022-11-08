# import
# import tkinter as gui
# from tkinter import Frame, filedialog, ttk
import mysql.connector as sql
import os
from others.SQLGen import *
from others.authCheck import *
from itemFile import *
from peopleList import *
import Export_Item
# from PIL import ImageTk, Image
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


def startPage():
    # global root
    # root.destroy()
    root = customtkinter.CTk()
    root.geometry("1280x720")
    root.resizable(False, False)
    authPage = customtkinter.CTkToplevel()
    authFrame = customtkinter.CTkFrame(master= authPage, width=450, height=120, borderwidth=0)
    authFrame.pack()
    customtkinter.CTkLabel(master= authFrame, text="User ID").grid(row=0,
                                                           column=0,
                                                           sticky="w")
    customtkinter.CTkLabel(master= authFrame, text="Password").grid(row=1,
                                                            column=0,
                                                            sticky="w")
    userID_val = customtkinter.CTkEntry(master= authFrame)
    userID_val.grid(row=0, column=1)
    userPass_val = customtkinter.CTkEntry(master= authFrame)
    userPass_val.grid(row=1, column=1)
    authPage.geometry()
    customtkinter.CTkButton(master= authFrame, text="Submit",
                            # command=lambda: (authPage.quit(), mainPage()) if authCheck(getFields(buttonList)) == True
                            # else customtkinter.CTkLabel(authFrame, text="Incorrect Credentials")
                            # .grid(row=3, columnspan=2)
                            ).grid(row=2, column=0, pady=2)
    customtkinter.CTkButton(master= authFrame, text="Clear Fields", width=25
                            # , command=lambda: clearFields(buttonList)
                            ).grid(row=2, column=1, pady=2)
    authPage.resizable(False, False)
    authPage.mainloop()
    root.mainloop()


def learning():
    root = customtkinter.CTk()
    root.config()
    root.title("learning")
    root.geometry("640x360")
    root.resizable(0, 0)
    frame = customtkinter.CTkFrame(master= root, bg_color="white")
    frame.place()

    root.mainloop()


startPage()
