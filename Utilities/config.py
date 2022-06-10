# This python file is a library to add reusable methods
import configparser

import mysql.connector
#We need to import errors to see the error in log
from mysql.connector import Error
import maskpass
pwd = maskpass.askpass(mask="")

def getConfig():
    config = configparser.ConfigParser()
    config.read("Utilities/properties.ini")
    return config


connect_config = {
    'user': getConfig()['SQL']['user'],
    'password': pwd,
    'host': getConfig()['SQL']['host'],
    'database':getConfig()['SQL']['database']
}

# We can add **, it means that the argument is a dict
def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("connection is successful")
            return conn
    except Error as e:
        print(e)

# Method to get a query from db and return a tuple, remember dont hardcode the query use it as a parameter
def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    print(row)
    conn.close()
    return row


