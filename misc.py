import requests

# Cookie sample in https://rahulshettyacademy.com/
# The visit-month cookie tracks the month of the user and if it landed on a month without updates it will
# load faster with cache info from last time the user visited, but if there is update,
# then it will load new info and load slower
cookie = {"visit-month":"February"}
response = requests.get("https://rahulshettyacademy.com/", cookies=cookie)
print(response.status_code)

# 2nd cookie sample to track a cookie response (not every interaction with cookies has a response!)
# usually info on text would be html but some websites has exclusive cookie info
# We can also use sessions with cookies
se = requests.session()
se.cookies.update({"visit-month":"May"})
res = se.get("https://httpbin.org/cookies", cookies={"visit-year":"2022"})
print(response.history)
print(res.text)

# Sample to review redirects, initially a website might go to another website before the requested endpoint
# there are dif reasons for this including security at the begining, so the status code initially could be
# 301 and then change to 200, usually status code shows the last code. to see redirections we can use
# response.history or allow redirects to false (if there is redirection stop it)
response = requests.get("https://geeksforgeeks.org/", allow_redirects=False)
print(response.history)
print(response.status_code)
response = requests.get("https://geeksforgeeks.org/")
print(response.history)
print(response.status_code)

# Sample to use timeouts, will wait some time to take the response back, this should fail because we added very fast
# timeout
# response = requests.get("https://geeksforgeeks.org/", allow_redirects=False, timeout=0.1)
print(response.history)
print(response.status_code)

# Sample to upload attachment
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
file = {"file": open("C:\\Users\\victo\\Documents\\PythonProjectsPyCharm\\BackEndTesting\\courses.json", "rb")}
r = requests.post(url, files = file)
print(r.status_code)
print(r.text)