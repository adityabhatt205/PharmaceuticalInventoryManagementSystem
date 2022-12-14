import mysql.connector as sql
import csv

with open(r"others\passwordSQL.csv") as passpicker:
    kilo = csv.reader(passpicker)
    l = None
    for i in kilo:
        l = i
    sqlUser = l[0]
    sqlPass = l[1]
sqlHost = "localhost"
sql_auth_plugin = "mysql_native_password"


def AddPurReg(criteria='Billno', value='0'):
    con = sql.connect(host=sqlHost, user=sqlUser, passwd=sqlPass, auth_plugin=sql_auth_plugin, database="SQL_Project")
    cur = con.cursor()
    cur.execute(f"""
        SELECT SCName,Billno,Billdate,Itemname,Itemtype,Rate,Qty,Total FROM suppcust B,invoice I WHERE B.FirmID=I.FirmID AND SCCategory='S' AND {criteria} LIKE '{value}'
    """)
    results = cur.fetchall()
    cur.close()
    con.close()
    return results
