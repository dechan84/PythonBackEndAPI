# Lets add some hooks to our features
# delete a book after adding it from features
# the method name needs to be after_scenario, for more info check https://behave.readthedocs.io/en/stable/api.html
import requests

from Utilities.config import getConfig
from Utilities.resources import ApiResources


def after_scenario(context, scenario):
    if "library" in scenario.tags:

        context.urldelete = getConfig()['API']['endpoint'] + ApiResources.deleteBook
        deleteBook_response = requests.post(context.urldelete, json={"ID": context.bookId}, headers=context.myheaders, )
        assert deleteBook_response.status_code == 200
        print(deleteBook_response.json()["msg"])
        assert deleteBook_response.json()["msg"] == "book is successfully deleted"

