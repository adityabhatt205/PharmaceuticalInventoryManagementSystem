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


import mysql.connector as sql, random as rand, math as math, statistics as stat, pandas as pd


class cread:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.passwd = "root"
        self.database = "Hello"


def SQLCont(a):
    con = sql.connect(host=a.host, user=a.user, passwd=a.passwd, database=a.database)
    if con.is_connected():
        return con
    else:
        return False


def nameGen(i, a, table):
    a.execute(
        f"""
        DELETE FROM {table};
    """)
    blg = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', ' ']
    for alpha in range(i):
        nam = ""
        for pi in range(10):
            kilo = rand.randint(1, len(let) - 1)
            nam += let[kilo]
        clas = 12
        bldgrp = blg[rand.randint(0, len(blg) - 1)]
        a.execute(
            """
                INSERT INTO %s (sno, nam, class, bloodgrp) VALUE ('%s','%s','%s','%s');
            """ % (table, alpha + 1, nam.strip(), clas, bldgrp))


def cont(a, table):
    a.execute(
        f"""
    SELECT * FROM {table}
    """)
    extra = cur.fetchall()
    return extra


cred = cread()
con = SQLCont(cred)
cur = con.cursor()
nameGen(1000, cur, "item")
con.commit()
kilo = cont(cur, "MadeWithPy")
for i in kilo:
    for j in i:
        print(j, end='\t\t')
    print()

con.close()

print(round(math.sqrt(15), 2))
for i in range(20):
    print(rand.randint(0, 9))
