# import
from tkinter import filedialog
import os
from others.SQLGen import *
from files.itemFile import *
from peopleList import *
import csv


# variables
mainMessage = "Welcome to the Pharmaceutical Inventory Management System!"
mainItem = "Item File"
gui_bgColor = '#262626'
gui_fgColor = '#9999ff'
gui_FontStyle = "Palatino"


# Main Segment
# itemFileRunner()
def exportItemCSV():
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM item
    """)
    fileName = '2022'
    path = filedialog.askdirectory(initialdir=os.getcwd(), title="Create CSV Backups")
    backupFile = str(path)+'/'+fileName+'.csv'
    if path != '':
        with open(backupFile, 'w', newline='') as csvFile:
            file = csv.writer(csvFile)
            for i in cur.fetchall():
                print(i)
                file.writerow(i)
    con.close()
    cur.close()
