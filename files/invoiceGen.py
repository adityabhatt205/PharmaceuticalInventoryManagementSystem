# Invoice Generator

# Importing
import mysql.connector as sql

# Global Variables
sqlUser = "root"
sqlPass = "leviackerman"
sqlHost = "localhost"
sql_auth_plugin = "mysql_native_password"

# Functions
# noinspection SqlResolve
def invoiceSearch(criteria='FirmID', value='0'):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    value += '%'
    cur.execute(
        f"""
            SELECT * FROM invoice
            WHERE {criteria} LIKE {value}
        """
    )
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


# noinspection SqlResolve
def invoiceAdder(infoList):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO invoice values ({infoList})
    """)
    con.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


# noinspection SqlResolve
def invoiceDelete(firm):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
            DELETE FROM invoice WHERE FirmID = {firm}
        """)
    con.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results

def invoiceModify(valueFirmID):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    # noinspection SqlResolve
    cur.execute(
        f"""
            UPDATE invoice
            SET
                FirmID = {valueFirmID[0]},
                Firmname = {valueFirmID[1]},
                Billno = {valueFirmID[2]},
                Billdate = {valueFirmID[3]},
                Itemname = {valueFirmID[4]},
                Itemtype = {valueFirmID[5]},
                Batchno = {valueFirmID[6]},
                Packing = {valueFirmID[7]},
                Expdate = {valueFirmID[8]},
                Qty = {valueFirmID[9]},
                Rate = {valueFirmID[10]},
                Total = {valueFirmID[11]},
                Transport = {valueFirmID[12]}
            WHERE FirmID = {valueFirmID[0]}
        """
    )
    cur.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results
