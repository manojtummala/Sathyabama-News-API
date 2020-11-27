import requests
from bs4 import BeautifulSoup
import re

class News:
    @staticmethod
    def getevents() :

        response = {}
        url = 'https://sathyabama.ac.in/events'
        r = requests.get(url)
        # print(r.content)

        soup = BeautifulSoup(r.content, 'html5lib')
        # print(soup.prettify())

        events=[]
        # event = {}

        table = soup.find('div', attrs = {'class':'view-content'})
        # print(table.prettify)

        for time in table.findAll('div', attrs = {'class':'time'}):
            eventT={}
            eventT = time.text.strip()

        for venue in table.findAll('div', attrs = {'class':'venue'}):
            eventV = {}
            eventV = venue.text.strip()

        for title in table.findAll('div', attrs = {'class':'title'}):
            event={}
            event['Event'] = title.text.strip()
            event['Time'] = eventT
            event['Venue'] = eventV
            event['url'] = 'https://sathyabama.ac.in/' + title.a['href']
            events.append(event)



        # print(events)
        # response['count'] = len(event)
        response['list'] = events
        return(response)

    @staticmethod
    def getnews():
        response = {}
        url = 'https://sathyabama.ac.in/'
        r = requests.get(url)
        # print(r.content)

        soup = BeautifulSoup(r.content, 'html5lib')
        # print(soup.prettify())

        new = []

        table = soup.find('div', attrs = {'class':'view view-latest-news view-id-latest_news view-display-id-block_1 js-view-dom-id-2a4d342d0a75f95a8fd24a9e0c1443d7ff57c119c916ccd26ee73b7c6a763806'})
        # print(table.prettify)

        for time in table.findAll('time'):
            newsT ={}
            newsT = time.text.strip()

        for more in table.findAll('div', attrs = {'class':'view-more-right'}):
            newsU = {}
            newsU = 'https://sathyabama.ac.in' + more.a['href']

        for field in table.findAll('div', attrs = {'class':'title'}):
            news = {}
            news['News'] = field.text.strip()
            news['Time'] = newsT
            news['Read More'] = newsU

            new.append(news)

        # print(new)
        # response['count'] = len(news)
        response['list'] = new
        return(response)




        
        
            

