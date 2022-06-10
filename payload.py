# Add book payloads
# First sample is with hardcoded values
from Utilities.config import getQuery


def addBookPayload(isbn):
    body = {
        "name": "API Python8",
        "isbn": isbn,
        "aisle": "2270008",
        "author": "Javier Chan"
    }
    return body

def addBookPayload2(isbn, aisle):
    body = {
        "name": "API Python8",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Javier Chan"
    }
    return body
# Second sample is with dynamic values from db

def buildPayLoadFromDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody

