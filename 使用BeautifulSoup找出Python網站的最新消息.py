import requests
from bs4 import BeautifulSoup as soup
import time
url='http://www.python.org/'
def getnews(url):
    page = requests.get(url).text
    htm=soup(page,'html.parser')
    items = [elem for elem in htm.find_all('div', class_='shrubbery') ]
    for item in items:
        if item.h2.contents[1] == 'Latest News':
            ys = [y for y in item.find_all('li')]
            for y in ys:
                time = y.time['datetime']
                link = y.a['href']
                title = y.a.string
                print("時間：{}\n標題：{}\n連結：{}\n".format(time, title, link))
getnews(url)
