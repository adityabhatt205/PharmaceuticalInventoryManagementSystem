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


def itemFileRunner(check):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    if not check:
        cur.execute('''
            CREATE table item (
                itemID int,
                itemName varchar(50),
                itemCategory varchar(1),
                company varchar(50),
                composition text,
                rate decimal,
                stockist decimal,
                retailPrice decimal,
                mrp decimal,
                packing varchar(10),
                batchNo int,
                expiryDate date,
                manufacturingDate date
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
        cur.commit()
    cur.execute("""
        CREATE DATABASE SQL_Project
    """)
