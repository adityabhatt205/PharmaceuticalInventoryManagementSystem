# Importing
import mysql.connector as sql
import csv

# Global Variables
with open(r"others\passwordSQL.csv") as passpicker:
    kilo = csv.reader(passpicker)
    l = None
    for i in kilo:
        l = i
    sqlUser = l[0]
    sqlPass = l[1]
sqlHost = "localhost"
sql_auth_plugin = "mysql_native_password"


# Functions
# noinspection SqlResolve
def firmSearch(criteria='FirmID', value='0'):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    value += '%'
    value = '%' + value
    cur.execute(
        f"""
            SELECT * FROM suppcust
            WHERE {criteria} LIKE '{value}'
        """
    )
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


# noinspection SqlResolve
def peopleAdder(infoList):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    print(infoList)
    cur.execute(f"""
        INSERT INTO suppcust values {infoList}
    """)
    con.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


# noinspection SqlResolve
def peopleDelete(People):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
            DELETE FROM suppcust WHERE ID = {People}
        """)
    con.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


def peopleModify(valuePeopleID):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    # noinspection SqlResolve
    cur.execute(
        f"""
            UPDATE suppcust
            SET
                ID = {valuePeopleID[0]},
                pName = {valuePeopleID[1]},
                pCategory = {valuePeopleID[2]},
                contactPerson = {valuePeopleID[3]},
                address = {valuePeopleID[4]},
                city = {valuePeopleID[5]},
                pinCode = {valuePeopleID[6]},
                proprietor = {valuePeopleID[7]},
                phoneNo = {valuePeopleID[8]},
                mobileNo = {valuePeopleID[9]},
                gstNo = {valuePeopleID[10]},
                dlNo = {valuePeopleID[11]}
            WHERE ID = {valuePeopleID[0]}
        """
    )
    cur.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results
