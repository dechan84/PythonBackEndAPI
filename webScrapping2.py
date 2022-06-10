import requests
from bs4 import BeautifulSoup

data = requests.get("https://rahulshettyacademy.com/AutomationPractice/")
# If we want to know the body of the response we use content, we also select the parser, in this sample use html
soup = BeautifulSoup(data.content, "html.parser")
print(soup.prettify())
# Get the content from Appium string
appiumData = soup.find('a',string='Appium')
print(appiumData['href'])