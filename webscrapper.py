import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3 as lite


theUrl = 'https://www.lindaikejisblog.com/'
page = requests.get(theUrl)
soup = BeautifulSoup(page.content,"html.parser")
results = soup.find_all('article',class_='story_block')

records =[]
for result in results:
    headline = result.a.text
    images = result.img.get('src')
    story = result.p.text
    records.append((headline,images,story))


df = pd.DataFrame(records, columns=['headline','images','story'])
df.to_csv('data.csv', index = False, encoding = 'utf-8')
