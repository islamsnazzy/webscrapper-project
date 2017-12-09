import pymysql
from bs4 import BeautifulSoup as bs
import requests

Urllinks = ['https://www.gsmarena.com','https://www.reuters.com/news/archive/businessNews?view=page','http://www.goal.com/en-ng','https://www.nigerianbulletin.com/forums/political-news.2/']
for urls in Urllinks:
    thePage = requests.get(urls)
    soup = bs(thePage.content,"html.parser")

    tech_result = soup.find_all('div',class_='news-item')
    for tech_data in tech_result:
        tech_news = 'www.gsmarena.com/{}'.format(tech_data.a.get('href'))
       

    finance_result = soup.find_all('div',class_='story-content')
    for finance_data in finance_result:
        finance_news = 'www.reuters.com' + finance_data.a.get('href')
       

    sport_result = soup.find_all('div',class_='type-article')
    for sport_data in sport_result:
        sport_news = sport_data.a.get('href')
        

    politics_result= soup.find_all('a',class_='PreviewTooltip')
    for politics_data in politics_result:
        politics_news = 'www.nigerianbulletin.com/{}'.format(politics_data.get('href'))
        

def open_database():
    db = pymysql.connect('localhost','abdulsalam1','snazzy1','dbproject')
    print("connected successfully")
    db.close()
def create_table():
    db = pymysql.connect('localhost','abdulsalam1','snazzy1','dbproject')
    print("connected successfully")
    cur = db.cursor()
    sql = """CREATE TABLE CATEGORY(
            TECHNEWS TEXT,
            SPORTNEWS TEXT,
            FINANCENEWS TEXT,
            POLITICSNEWS TEXT)"""
    
    try:
        cur.execute(sql)
        print("table created successfully")
        db.commit()
    except:
        db.rollback()
    db.close()
def insert_table():
    db = pymysql.connect('localhost','abdulsalam1','snazzy1','dbproject')
    print("connected successfully")
    cur = db.cursor()
    sql= "INSERT INTO CATEGORY(TECHNEWS,\
            SPORTNEWS,FINANCENEWS,POLITICSNEWS)\
            VALUES('%s','%s','%s','%s')"%\
            (tech_news,sport_news,finance_news,politics_news)
    
    try:
        cur.execute(sql)
        print("inserted to table successfully")
        db.commit()
    except:
        db.rollback()
    db.close()

def retrieve_table(userInput):
    db = pymysql.connect('localhost','abdulsalam1','snazzy1','dbproject')
    print("connected successfully")
    cur = db.cursor()
    sql = "SELECT %s FROM CATEGORY"%(userInput)
    try:
        cur.execute(sql)
        results = cur.fetchone()
        for row in result:
            print ("%s" % (row[userInput]))
    except:
        print("not successful")
        db.close
def main():
    retrieve_table('SPORTNEWS')
main()










    
    
