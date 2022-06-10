import json
import requests

# Sending get to the api
# request.get requires 3 params, if you dont have the third one just leave it blank
response = requests.get("http://216.10.245.166/Library/GetBook.php",
             params={"AuthorName":"Victor Chan Cheng"},)

# Lets see the response from api in text
print(response.text)
print(type(response.text))
# Loads figures out if there is a list in the dict and will convert it
dict_response = json.loads(response.text)
# Lets print isbn
print(dict_response[0]["isbn"])
# There is another way to manage response in python using the response lib, we an then ignore json.loads
# Instead of converting into dict we can read it directly into json
json_response = response.json()
print(json_response)

# We can also validate response status codes, 200 is success
assert response.status_code == 200
# Access to headers in the response object
print(response.headers)
# Example, lets validate content-type header
assert response.headers["Content-Type"] == "application/json;charset=UTF-8"

# Retreive the book with the isbn : bcd1116, assuming author is Victor
response2 = requests.get("http://216.10.245.166/Library/GetBook.php",
             params={"AuthorName":"Victor"},)
# print(response.text)
json_response2 = response2.json()
for book in json_response2:
    if book["isbn"] == "bcd1116":
        print(book)
        actual_book = book

expected_book = {
                 'book_name': 'API Python6',
                 'isbn': 'bcd1116',
                 'aisle': '2270006'
                 }

assert expected_book == actual_book