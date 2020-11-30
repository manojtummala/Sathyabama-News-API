import requests
from bs4 import BeautifulSoup
import re

class News:
    @staticmethod
    def getevents() :

        response = {}
        response['list'] = []

        url = 'https://sathyabama.ac.in/events'
        r = requests.get(url)
        # print(r.content)

        soup = BeautifulSoup(r.content, 'html5lib')
        # print(soup.prettify())

        eventList=[]
        timeList = []
        venueList = []
        urlList = []

        table = soup.find('div', attrs = {'class':'view-content'})
        # print(table.prettify)

        for time in table.findAll('div', attrs = {'class':'time'}):
            timeList.append(time.text.strip())

        for venue in table.findAll('div', attrs = {'class':'venue'}):
            venueList.append(venue.text.strip())

        for title in table.findAll('div', attrs = {'class':'title'}):
            eventList.append(title.text.strip())
            urlList.append('https://sathyabama.ac.in/' + title.a['href'])

        for i in range(0,len(eventList)):
            row = {}
            row['News'] = eventList[i]
            row['Time'] = timeList[i]
            row['Venue'] = venueList[i]
            row['URL'] = urlList[i]
            response['list'].append(row)
   
        return(response)

    @staticmethod
    def getnews():
        response = {}
        response['list'] = []

        url = 'https://sathyabama.ac.in/'
        r = requests.get(url)
        # print(r.content)

        soup = BeautifulSoup(r.content, 'html5lib')
        # print(soup.prettify())

        newsList = []
        timeList = []
        urlList = []

        table = soup.find('div', attrs = {'class':'view view-latest-news view-id-latest_news view-display-id-block_1 js-view-dom-id-2a4d342d0a75f95a8fd24a9e0c1443d7ff57c119c916ccd26ee73b7c6a763806'})
        # print(table.prettify)
            
        for field in table.findAll('div', attrs = {'class':'title'}):
            newsList.append(field.text.strip())

        for time in table.findAll('div', attrs={'class': 'date'}):
            timeList.append(time.text.strip())

        for more in table.findAll('div', attrs = {'class':'view-more-right'}):
            urlList.append('https://sathyabama.ac.in' + more.a['href'])

        for i in range(0,len(newsList)):
            row = {}
            row['News'] = newsList[i]
            row['Time'] = timeList[i]
            row['URL'] = urlList[i]
            response['list'].append(row)

        # print(response)
        return(response)




        
        
            

