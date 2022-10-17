# Importing
import mysql.connector as sql

# Global Variables
sqlUser = "root"
sqlPass = "root"
sqlHost = "localhost"
sql_auth_plugin = "mysql_native_password"


# Functions
def itemSearch(criteria='itemNo', value='0'):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    value += '%'
    cur.execute(
        f"""
            SELECT * FROM item
            WHERE {criteria} LIKE {value}
        """
    )
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


def itemAdder(list):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO item values ({list})
    """)
    con.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


def itemDelete(valueItemID):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
            DELETE FROM item WHERE itemID = {valueItemID}
        """)
    con.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


def itemModify(valueItemID):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(
        f"""
            UPDATE item
            SET
                itemID = {valueItemID[0]},
                itemName = {valueItemID[1]},
                itemCategory =  {valueItemID[2]},
                company = {valueItemID[3]},
                compositio = {valueItemID[4]},
                rate = {valueItemID[5]},
                stockist = {valueItemID[6]},
                retailPrice = {valueItemID[7]},
                mrp = {valueItemID[8]},
                packing = {valueItemID[9]},
                batchNo = {valueItemID[10]},
                expiryDate = {valueItemID[11]},
                manufacturingDate = {valueItemID[12]}
            WHERE itemID = {valueItemID[0]}
        """
    )
    cur.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results
