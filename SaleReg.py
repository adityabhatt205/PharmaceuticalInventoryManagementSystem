
import mysql.connector as sql

sqlUser = "root"
sqlPass = "leviackerman"
sqlHost = "localhost"
sql_auth_plugin = "mysql_native_password"

def AddSaleReg():
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute("""
        SELECT SCName,Billno,Billdate,Itemname,Itemtype,Rate,Qty,Total FROM suppcust B,invoice I WHERE B.FirmID=I.FirmID AND SCCategory='C'
    """)
    results = cur.fetchall()
    cur.close()
    con.close()
    return results
