# Importing
import mysql.connector as sql

# Global Variables
sqlUser = "root"
sqlPass = "root"
sqlHost = "localhost"
sql_auth_plugin = "mysql_native_password"


# Functions
def peopleSearch(criteria='peopleNo', value='0'):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    value += '%'
    cur.execute(
        f"""
            SELECT * FROM people
            WHERE {criteria} LIKE {value}
        """
    )
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


def peopleAdder(list):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO people values ({list})
    """)
    con.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


def peopleDelete(People):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
            DELETE FROM people WHERE itemID = {People}
        """)
    con.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


def peopleModify(valuePeopleID):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(
        f"""
            UPDATE people
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
            WHERE itemID = {valuePeopleID[0]}
        """
    )
    cur.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results
