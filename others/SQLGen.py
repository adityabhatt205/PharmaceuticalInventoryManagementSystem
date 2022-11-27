# Importing
import mysql.connector as sql
import csv

# Global Variables
with open(r"passwordSQL.csv") as passpicker:
    kilo = csv.reader(passpicker)
    l = None
    for i in kilo:
        l = i
    sqlUser = l[0]
    sqlPass = l[1]
sqlHost = "localhost"
sql_auth_plugin = "mysql_native_password"


# Functions
def reset():
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin)
    cur = con.cursor()
    if checker():
        cur.execute("""
            DROP DATABASE SQL_Project
        """)
        con.commit()
    cur.execute("""
        CREATE DATABASE SQL_Project
    """)
    con.commit()
    itemMasterFileRunner()
    SuppCustRunner()
    invoiceGenRunner()
    stockRegRunner()


def checker():  # -----> if SQL_Project exists: True or False
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin)
    cur = con.cursor()
    try:
        cur.execute('''USE SQL_Project''')
        return True
    except sql.errors.ProgrammingError:
        return False


def itemMasterFileRunner():
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute('''
        CREATE table item (
            itemID int primary key,                                     /*  0   */
            itemName varchar(50),                                       /*  1   */
            itemCategory varchar(1),                                    /*  2   */
            company varchar(50),                                        /*  3   */
            composition text,                                           /*  4   */
            stockist decimal(8,2),                                      /*  5   */
            retailPrice decimal(8,2),                                   /*  6   */
            mrp decimal(8,2),                                           /*  7   */
            packing varchar(10)
        )
    ''')
    con.commit()
    return True


def SuppCustRunner():
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute('''
        CREATE table SuppCust (
            firmID int primary key,                                 /*  0   */
            SCName varchar(50),                                     /*  1   */
            SCCategory varchar(1),                                  /*  2   */
            contactPerson varchar(50),                                      /*  3   */
            address varchar(50),                                    /*  4   */
            city varchar(50),                                       /*  5   */
            pinCode int,                                            /*  6   */
            proprietor varchar(15),                                 /*  7   */
            phoneNo varchar(10),                                            /*  8   */
            mobileNo varchar(10),                                           /*  9   */
            gstN int,                                               /*  10  */
            dlNo int                                                /*  11  */
        )
    ''')
    con.commit()
    return True


def invoiceGenRunner():
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute('''
        CREATE table invoice (
            firmID int,                                               /*  0   */
            firmName varchar(50),                                     /*  1   */
            billNo int,                                               /*  2   */
            billDate date,                                            /*  3   */
            itemName varchar(50),                                     /*  4   */
            itemType varchar(50),                                     /*  5   */
            batchNo int,                                              /*  6   */
            packing varchar(10),                                      /*  7   */
            expDate date,                                             /*  8   */
            qty int,                                                  /*  9   */
            rate int,                                                 /*  10  */
            total int,                                                /*  11  */
            transport varchar(50)                                     /*  12  */
        )
    ''')
    con.commit()
    return True


def stockRegRunner():
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute('''
        CREATE table StockRegister (
            item varchar(50),                                              /*  0   */
            itemType varchar(50),                                          /*  1   */
            batchNo int,                                                   /*  2   */
            packing varchar(50),                                           /*  3   */
            expDate date,                                                  /*  4   */
            rate int,                                                      /*  5   */
            qty int                                                        /*  6   */
        )
    ''')
    con.commit()
    return True

