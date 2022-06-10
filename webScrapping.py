# Sample to do web scrapping with beautiful soup
# Warning: Some websites use JS that hides the html raw body so we are no allowed to do web scrapping
import requests
from bs4 import BeautifulSoup

li=[]
data = requests.get("https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm")
# If we want to know the body of the response we use content, we also select the parser, in this sample use html
soup = BeautifulSoup(data.content, "html.parser")
# print(soup.prettify())
# The find option uses the tag argument and then we can pass attributes
moviesTable = soup.find('table', {'class':'findList'})
# print(moviesTable.prettify())
# Lets keep narrowing the results to filter info and get all the data from tr tag
rows = moviesTable.findAll('tr')
for row in rows:
    rowdata = row.findAll('td')
    title = rowdata[1].a.text
    # print('TV series Name: '+title)
    # Get the url from each title
    suburl = rowdata[1].a['href']
    subdata = requests.get('https://www.imdb.com/'+suburl)
    # print(suburl)
    # Now we parse the content of each thriller webpage into childSoup list
    childSoup = BeautifulSoup(subdata.content, 'html.parser')
    # Lets access the url link in each title and get all the genres in a tv series
    genrediv = childSoup.find('div', {'data-testid': 'genres'})
    if genrediv:
        genres = genrediv.findAll('a')
        for genre in genres:
            # Lets increase the filtering by only print tv series with genre equal to documentary
            if genre.ul.li.text == 'Documentary':
                print('TV Series Name: ' + title)
                print('Genre Name: '+genre.ul.li.text)
                li.append(title)
print(li)



