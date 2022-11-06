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


def peopleListRunner(check):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    if not check:
        cur.execute('''
            CREATE table people (
                ID int primary key,                                     /*  0   */
                pName varchar(50),                                      /*  1   */
                pCategory varchar(1),                                   /*  2   */
                contactPerson int,                                      /*  3   */
                address varchar(50),                                    /*  4   */
                city varchar(50),                                       /*  5   */
                pinCode int,                                            /*  6   */
                proprietor varchar(15),                                 /*  7   */
                phoneNo int,                                            /*  8   */
                mobileNo int,                                           /*  9   */
                gstN int,                                               /* 10   */
                dlNo int                                                /* 11   */
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


reset()
# checker()
itemFileRunner()
peopleListRunner(False)
