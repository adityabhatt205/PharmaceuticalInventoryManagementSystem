# Importing
import mysql.connector as sql

# Global Variables
sqlUser = "root"
sqlPass = "leviackerman"
sqlHost = "localhost"
sql_auth_plugin = "mysql_native_password"


# Functions
# noinspection SqlResolve
def SCSearch(criteria='SCNo', value='0'):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    value += '%'
    cur.execute(
        f"""
            SELECT * FROM suppcust
            WHERE {criteria} LIKE {value}
        """
    )
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


# noinspection SqlResolve
def SCAdder(infoList):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO suppcust values ({infoList})
    """)
    con.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


# noinspection SqlResolve
def SCDelete(People):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
            DELETE FROM suppcust WHERE FirmID = {People}
        """)
    con.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results


def SCModify(valueSCID):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    # noinspection SqlResolve
    cur.execute(
        f"""
            UPDATE suppcust
            SET
                FirmID = {valueSCID[0]},
                pName = {valueSCID[1]},
                pCategory = {valueSCID[2]},
                contactPerson = {valueSCID[3]},
                address = {valueSCID[4]},
                city = {valueSCID[5]},
                pinCode = {valueSCID[6]},
                proprietor = {valueSCID[7]},
                phoneNo = {valueSCID[8]},
                mobileNo = {valueSCID[9]},
                gstNo = {valueSCID[10]},
                dlNo = {valueSCID[11]}
            WHERE ID = {valueSCID[0]}
        """
    )
    cur.commit()
    results = cur.fetchall()
    cur.close()
    con.close()
    return results
