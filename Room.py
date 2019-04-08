#!/Users/sinch/AppData/Local/Programs/Python/Python37-32/python

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
RID = form.getvalue('RID')
FLOOR = form.getvalue('FLOOR')
ROOM_TYPE = form.getvalue('ROOM_TYPE')
NO_OF_BEDS= form.getvalue('NO_OF_BEDS')
PRICE = form.getvalue('PRICE')
OCCUPANCY = form.getvalue('OCCUPANCY')
WIFI = form.getvalue('WIFI')
TV = form.getvalue('TV')
BREAKFAST = form.getvalue('BREAKFAST')
AC = form.getvalue('AC')
START_DT=form.getvalue('START_DT')
END_DT=form.getvalue('END_DT')
PCID = form.getvalue('Phone_no')




import pymysql
db = pymysql.connect("localhost","root","Welcome1","HOTEL_DB" )
cursor = db.cursor()
#data =cursor.execute("select max(PCID)+1 from pcustomer")
#print("your customer ID is :",data)
cursor.execute("INSERT INTO ROOMS(RID,FLOOR,ROOM_TYPE,NO_OF_BEDS,PRICE,OCCUPANCY,WIFI,TV,BREAKFAST,AC) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(RID,FLOOR,ROOM_TYPE,NO_OF_BEDS,PRICE,OCCUPANCY,WIFI,TV,BREAKFAST,AC))
cursor.execute("INSERT INTO BOOKINGS(PCID,RID,START_DT,END_DT,PAY_ID,FINAL_PRICE) VALUES (%s,%s,%s,%s,%s,%s)",(PCID,RID,START_DT,END_DT,PCID,PRICE))
db.commit()


# Execute SQL select statement
room_query="SELECT DISTINCT R.RID,R.FLOOR,R.ROOM_TYPE,R.NO_OF_BEDS,R.PRICE,R.OCCUPANCY,R.WIFI,R.TV,R.BREAKFAST,R.AC FROM ROOMS R WHERE TRUE"
cursor.execute(room_query)

# Get the number of rows in the resultset
data = cursor.fetchall()
attribute_names = [i[0] for i in cursor.description]
print("<p>Room Details</p>")
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

booking_query="SELECT DISTINCT B.PCID,B.RID,B.START_DT,B.END_DT,B.PAY_ID,B.FINAL_PRICE FROM BOOKINGS B WHERE B.PCID=%s";
cursor.execute(booking_query,PCID)

# Get the number of rows in the resultset
data = cursor.fetchall()
attribute_names = [i[0] for i in cursor.description]
print("<p>Booking Details</p>")
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