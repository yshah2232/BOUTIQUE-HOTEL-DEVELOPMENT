#!/Users/sinch/AppData/Local/Programs/Python/Python37-32/python

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
name = form.getvalue('name')
Age = form.getvalue('Age')
Phone_no = form.getvalue('Phone_no')
Government_ID= form.getvalue('Government_ID')
P_Phone_no = form.getvalue('Primary_Phone_no')


import pymysql
db = pymysql.connect("localhost","root","Welcome1","HOTEL_DB" )
cursor = db.cursor()
#data =cursor.execute("select max(PCID)+1 from pcustomer")
#print("your customer ID is :",data)
cursor.execute("INSERT INTO DEPENDANTS(DCID,Name,Age,GOVT_ID,PHONE,PCID) VALUES (%s,%s,%s,%s,%s,%s)",(Phone_no,name,Age,Government_ID,Phone_no,P_Phone_no))
db.commit()

cursor = db.cursor()

# Execute SQL select statement
sql_query="SELECT DISTINCT D.DCID,D.Name,D.Age,D.GOVT_ID,D.PHONE,D.PCID FROM DEPENDANTS D WHERE TRUE"
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