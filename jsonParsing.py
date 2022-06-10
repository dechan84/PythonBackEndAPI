# Package that parse json
import json

courses = '{"name": "VictorChan","languages":["Java","Python"]}'

# Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type (dict_courses))
print(dict_courses)

# Print values from the dictionary, get the first language
# Method 1
print(dict_courses['languages'])
languages = dict_courses['languages']
print(languages[0]) # Print Java

# Method 2
print(dict_courses['languages'][1]) # Print Python

# Open a json file and then parse it
with open('courses.json') as f:
    # Load takes a file and convert it in dict
    data = json.load(f)
    print(data)

# Example, now parse the second course information from courses.json
    print('2nd course info: ')
    print(data['courses'][1])
    print('2nd course title: ' )
    print(data['courses'][1]['title'])
# Example, now parse the dashboard website from courses.json
    print(data['dashboard']['website'])
# Example, get the price of third course with a nested structure, consider data as a list
    for course in data['courses']:
        if course['title'] == 'RPA':
            print(course['price'])
            assert course['price'] == 45
# Example compare json files
# Reuse f as the object of the first json file to compare
# Create g as the object of the secong json file to compare
with open('courses1.json') as g:
    # Load takes a file and convert it in dict
    data2 = json.load(g)
    # The assert should fail because they are different files
    assert data == data2


