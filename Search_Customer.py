#!C:/Users/deeps/AppData/Local/Programs/Python/Python37-32/python.exe -u
print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
p_cid = form.getvalue('pcid')


import pymysql
db = pymysql.connect("localhost","root","123456789","HOTEL_DB" )
cursor = db.cursor()

# Execute SQL select statement
cursor.execute("select * from bookings where pcid = (%s)",p_cid)

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