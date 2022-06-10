# Here are the methods to be implemented in .feature
# context parameter is mandatory in each method is like a global properties that contains all parameters in the file
# Sample if for a POST cmd to add a book
import requests
from behave import *

import payload
from Utilities.config import getConfig
from Utilities.resources import ApiResources


# given is to add variables
@given('the Book details which needs to be added to Library with ID {myID:d}')
def step_impl(context, myID):
    context.urladd = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.myheaders = {"Content-Type": "application/json"}
    context.payload = payload.addBookPayload(myID)

# given is to add execution
@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.urladd, json=context.payload, headers=context.myheaders, )


# then is assertion or validations
@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json["ID"]
    print(context.bookId)
    assert response_json["Msg"] == "successfully added"

@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.urladd = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.myheaders = {"Content-Type": "application/json"}
    context.payload = payload.addBookPayload2(isbn, aisle)


@given('I have github credentials')
def step_impl(context):
    context.api_token = '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'
    context.se = requests.session()
    context.se.auth = ('dechan84', context.api_token)


@when('When I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


# We can parametrize the steps description with {<name>:d or s} so we can change them in the feature file
@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode

