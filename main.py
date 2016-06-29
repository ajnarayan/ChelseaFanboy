import requests
#from scrapy.selector import HtmlXPathSelector
from bs4 import BeautifulSoup
import pynotify
from time import sleep

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

def print_not(url, title):
    while True:
        r = requests.get(url)
        while r.status_code is not 200:
            r = requests.get(url)

    # response = r.text
    # xxs = HtmlXPathSelector(text= response)
    # news = '\n'.join(xxs.select('//div[@class="score"]//a/text()').extract())
    # news =  news + '\n'.join(xxs.select('//div[@class="score"]//span/text()').extract()) + ' '
    # news =  news + '\n'.join(xxs.select('//div[@class="prev-score"]//text()').extract())
    # l=len(news)-2
    # sendmessage("IPL", news[:l])
    # sleep(5)
        soup = BeautifulSoup(r.text)
        data = soup.find_all("title")
        news = ""
        for i in range(2,len(data)):
            news = data[i].text + '\n'
            sendmessage(title, news)
        sleep(100)
    #to get only the top newsl replace for loop with data[1].text     

url = "http://www.dailymail.co.uk/sport/teampages/chelsea.rss"
url2 = "https://www.reddit.com/r/chelseafc/.rss"

print_not(url, "Daily Dose of Chelsea FC")