import requests
from bs4 import BeautifulSoup
import pandas as pd


#connection and parsing of website using requests and beautifulsoup
theUrl = 'https://www.lindaikejisblog.com/'
page = requests.get(theUrl)
soup = BeautifulSoup(page.content,"html.parser")

#gets specific html elements from parsed website and assigning them to a variable and then append in a list(seperated with commas)
results = soup.find_all('article',class_='story_block')
records =[]
for result in results:
    headline = result.a.text
    images = result.img.get('src')
    story = result.p.text
    records.append((headline,images,story))
   
#inserting each scrapped data into a dataframe with columns using pandas
df = pd.DataFrame(records, columns=['headline','images','story'])
df.to_csv('data.csv', index = False, encoding = 'utf-8')

#creating and populating into a database file using pandas
db = sqlite3.connect('lindadata.sqlite')
csv_file = pd.read_csv('data.csv')
csv_file.to_sql('lindadata',db)
