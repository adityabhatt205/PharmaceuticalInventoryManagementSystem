# Importing
import mysql.connector as sql

# Global Variables
sqlUser = "root"
sqlPass = "root"
sqlHost = "localhost"
sql_auth_plugin = "mysql_native_password"


# Functions
def checker():  # -----> if SQL_Project exists: True or False
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin)
    cur = con.cursor()
    try:
        cur.execute('''USE SQL_Project''')
        return True
    except sql.errors.ProgrammingError:
        cur.execute('''CREATE DATABASE SQL_Project''')
        con.commit()
        return False


def itemFileRunner():
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
            packing varchar(10),                                        /*  8   */
            batchNo int,                                                /*  9   */
            expiryDate date,                                            /* 10   */
            manufacturingDate date                                      /* 11   */
        )
    ''')
    con.commit()
    return True


def invoiceGenRunner(check):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    if not check:
        cur.execute('''
            CREATE table suppcust (
                FirmID int primary key,                                 /*  0   */
                SCName varchar(50),                                     /*  1   */
                SCCategory varchar(1),                                  /*  2   */    /* Supplier or customer (drop down menu) */
                contactPerson int,                                      /*  3   */
                address varchar(50),                                    /*  4   */
                city varchar(50),                                       /*  5   */
                pinCode int,                                            /*  6   */
                proprietor varchar(15),                                 /*  7   */
                phoneNo int,                                            /*  8   */
                mobileNo int,                                           /*  9   */
                gstN int,                                               /*  10  */
                dlNo int                                                /*  11  */
            )
        ''')
        con.commit()
    return True


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


def invoiceGenRunner(check):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    if not check:
        cur.execute('''
            CREATE table invoice (
                FirmID int,                                               /*  0   */
                Firmname varchar(50),                                     /*  1   */
                Billno int,                                               /*  2   */
                Billdate date,                                            /*  3   */
                Itemname varchar(50),                                     /*  4   */
                Itemtype varchar(50),                                     /*  5   */
                Batchno int,                                              /*  6   */
                Packing varchar(10),                                      /*  7   */
                Expdate date,                                             /*  8   */
                Qty int,                                                  /*  9   */
                Rate int,                                                 /*  10  */
                Total int,                                                /*  11  */
                Transport varchar(50)                                     /*  12  */
            )
        ''')
        con.commit()
    return True


def stockRegRunner(check):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    if not check:
        cur.execute('''
            CREATE table StockRegister (
                Item varchar(50),                                              /*  0   */
                Itemtype varchar(50),                                          /*  1   */
                Batchno int,                                                   /*  2   */
                Packing varchar(50),                                           /*  3   */
                Expdate date,                                                  /*  4   */
                Rate int,                                                      /*  5   */
                Qty int,                                                       /*  6   */
            )
        ''')
        con.commit()
    return True

# reset()
# checker()
# itemFileRunner()
# # stockRegRunner(False)
# invoiceGenRunner(False)
