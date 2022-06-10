# sample connecting to mysql db from python
import mysql.connector

# this methods requires host, database, auth, password
# conn = mysql.connector.connect(host="localhost", database="APIDevelop", user="root", password=pwd)
from Utilities.config import getConnection

# Optimizing the connector parameters from a method in Utilities
conn = getConnection()
print(conn.is_connected())

# Use cursor to execute queries
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
# Use cursor fetch to get the results, you can set the number of rows or all
row = cursor.fetchone()
print(row)
print("Print the third index: "+row[3])
# When fetching all it will fetch all the remaining information, based on the last entry of the pointer
# We fetched previously index 0 so now with fetch all it will not show up
allrows = cursor.fetchall()
print(allrows)
# Lets try to filter by col Ammount info
for col in allrows:
    print (col[2])

# Sample to show how to update a query use %s as parameter
query = "Update customerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")
# Python automatically knows that it needs to take this data tuple and add it in query
cursor.execute(query, data)
# We need to commit the query
conn.commit()

# Sample on how to delete
query2 = "delete from customerInfo where courseName = %s"
data2 = ["Jmeter"]
cursor.execute(query2, data2)
# We need to commit the query
conn.commit()
# After we got our queries we need to close the conn
conn.close()
