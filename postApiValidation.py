import requests
import json

# Last argument can be empty, headers too
# addBook_response = requests.post("http://216.10.245.166/Library/Addbook.php",
#                                 json={"name":"API Python8",
#                                       "isbn":"bcd1118",c
#                                       "aisle":"2270008",
#                                       "author": "Javier Chan"},
#                                 headers={"Content-Type" : "application/json"},)
# Using payloads instead of hardcoding the code in the test and also parametrize the server address with configparser
# Use the properties.ini for endpoints
import payload
from Utilities.config import getConfig
from Utilities.resources import *
#Valid only 30 days
api_token = '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'
# Use resources.py file to keep optimizing the test
urladd = getConfig()['API']['endpoint'] + ApiResources.addBook
myheaders = {"Content-Type" : "application/json"}
# Instead of using payload.addBookPayload lets use payload.buildPayLoadFromDB to send the query
query = "select * from Books"
# addBook_response = requests.post(urladd, json=payload.addBookPayload("ccc"), headers=myheaders,)
addBook_response = requests.post(urladd, json=payload.buildPayLoadFromDB(query), headers=myheaders,)
print(addBook_response.json())
response_json = addBook_response.json()
bookId = response_json["ID"]

# Lets try deleting the book now
urldelete = getConfig()['API']['endpoint'] + ApiResources.deleteBook

deleteBook_response = requests.post(urldelete, json={"ID": bookId}, headers=myheaders,)
assert deleteBook_response.status_code == 200
print(deleteBook_response.json()["msg"])
assert deleteBook_response.json()["msg"] == "book is successfully deleted"


#Authentication basic sample
# Request information on https://requests.readthedocs.io/
#Verify false for testing https and ignore verifications that can throw errors
# Never show the real password/user info when testing or uploading to git!
# Lets use session, to pass auth easily around access without the need to write it every time
se = requests.session()
se.auth = ('dechan84', api_token)

url = "https://api.github.com/user/"
# github_response = requests.get(url, headers={'Authorization': 'token '+api_token})
# github_response = requests.get(url, verify=False, auth=("dechan84", api_token))
github_response = se.get(url)
print(github_response.status_code)

url2 = "https://api.github.com/user/repos"
# response = requests.get(url2, auth=("dechan84", api_token))
response = se.get(url2)
print(response.status_code)