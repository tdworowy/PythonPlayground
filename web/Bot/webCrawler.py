import os
import re

import requests
from bs4 import BeautifulSoup


class crawler():
    def __init__(self):
        print("Start")

    def googleURL(self, find):
        return "https://www.google.pl?gws_rd=ssl#q={x}".format(x=find)

    def getLinksPages(self, URLs):
        if not isinstance(URLs, list):
            return self.getLinksPagesForBase(URLs)
        else:
            mapsList = []
            for baseURL in URLs:
                mapsList.append(self.getLinksPagesForBase(baseURL))
            return mapsList

    def getLinksPagesForBase(self, url):
        linksParent = self.getLinksPage(url)
        map_ = map(self.getLinksPage, linksParent)
        return (list(map_))

    def getLinksPage(self, link):
        links = []
        try:
            link = self.regexLinks(link)
            print(link[0])
            response = requests.get(link[0]).text
            soup = BeautifulSoup(response)
            links = soup.find_all("a", href=True)
        except Exception as ex:
            print(ex)
        return self.regexLinks(links)

    def regexLinks(self, text):
        all = re.findall(r'(https?://\S+)', str(text))
        map_ = map(self.cleanLink, all)
        list_ = list(map_)
        return list_

    def cleanLink(self, link):
        if ('>' in link): link = link[:link.index('>')]
        return link.replace("\"", "")

    def tofile(self,list):
        list = self.cleanList(list)
        path = os.path.dirname(os.path.abspath(__file__))
        f = open(path+"\\links.txt",'w')
        for line in list:
            f.write(line.strip()+'\n')
            f.flush()
        print("Links saved: "+str(len(list)))

    def cleanList(self,list):
         list = str(list).replace("[","").replace("]","")
         list=list.split(',')
         return list

def main():
    bot = crawler()
    googl = bot.googleURL("Tomasz Dworowy")
    linksList = bot.getLinksPages(googl)
    linksList2 = bot.getLinksPages(linksList)
    linksList3 = bot.getLinksPages(linksList2)
    linksList4 = bot.getLinksPages(linksList3)

    bot.tofile(linksList4)




if __name__ == "__main__":
    main()