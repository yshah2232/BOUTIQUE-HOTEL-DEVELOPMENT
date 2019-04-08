#!C:/Users/deeps/AppData/Local/Programs/Python/Python37-32/python.exe -u
print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
EVENT_ID = form.getvalue('EVENT_ID')
EVENT_TYPE = form.getvalue('EVENT_TYPE')
ARRANGEMENTS = form.getvalue('ARRANGEMENTS')
NO_OF_PPL= form.getvalue('NO_OF_PPL')
PCID=form.getvalue('PCID')
RID=form.getvalue('RID')
EVENT_DT=form.getvalue('EVENT_DT')

import pymysql
db = pymysql.connect("localhost","root","123456789","HOTEL_DB" )
cursor = db.cursor()
#data =cursor.execute("select max(PCID)+1 from pcustomer")
#print("your customer ID is :",data)

cursor.execute("INSERT INTO EVENT(EVENT_ID,EVENT_TYPE,ARRANGEMENTS,NO_OF_PPL,PCID,RID,EVENT_DT) VALUES (%s,%s,%s,%s,%s,%s,%s)",(EVENT_ID,EVENT_TYPE,ARRANGEMENTS,NO_OF_PPL,PCID,RID,EVENT_DT))
db.commit()

sql_query="SELECT DISTINCT E.EVENT_ID,E.EVENT_TYPE,E.ARRANGEMENTS,E.NO_OF_PPL,E.PCID,E.RID,E.EVENT_DT FROM EVENT E WHERE TRUE"
cursor.execute(sql_query)

# Get the number of rows in the resultset
data = cursor.fetchall()
attribute_names = [i[0] for i in cursor.description]

print("<style>table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%; } td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; } tr:nth-child(even) { background-color: #dddddd; } </style>")
print("<table><tr>")

for columns in attribute_names:
    print("<th>",columns,"</th>")
print ("</tr>")

for rows in data:
    print ("<tr>");
    for subrows in rows:
        print("<td>",subrows,"</td>")
    print ("</tr>")
print("</table>")