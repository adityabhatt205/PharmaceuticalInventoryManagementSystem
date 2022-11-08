# Importing
import mysql.connector as sql

# Global Variables
sqlUser = "root"
sqlPass = "root"
sqlHost = "localhost"
sql_auth_plugin = "mysql_native_password"


# Functions
# noinspection SqlResolve
def itemSearch(criteria='itemNo', value='0'):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    value += '%'
    value = '%' + value
    cur.execute(
        f"""
            SELECT * FROM item
            WHERE {criteria} LIKE '{value}'
        """
    )
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


# noinspection SqlResolve
def itemAdder(infoList):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO item values {infoList}
    """)
    con.commit()
    cur.close()
    con.close()


# noinspection SqlResolve
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


# noinspection SqlResolve
def itemModify(valueItemID):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(
        f"""
            UPDATE item
            SET
                itemID = {valueItemID[0]},
                itemName = {valueItemID[1]},
                itemCategory = {valueItemID[2]},
                company = {valueItemID[3]},
                composition = {valueItemID[4]},
                rate = {valueItemID[5]},
                retailPrice = {valueItemID[6]},
                mrp = {valueItemID[7]},
                packing = {valueItemID[8]},
                batchNo = {valueItemID[9]},
                expiryDate = {valueItemID[10]},
                manufacturingDate = {valueItemID[11]}
            WHERE itemID = {valueItemID[0]}
        """
    )
    cur.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


# itemAdder((
#     12,  # itemID
#     "Meds",  # itemName
#     "C",  # itemCategory
#     "TheCompany",  # company
#     "Something",  # composition
#     10.0,  # stockist
#     12.0,  # retailPrice
#     12.0,  # mrp
#     886275,  # packing
#     888289,  # batchNo
#     "20220808",  # expiryDate
#     "20220808"))  # manufacturingDate
