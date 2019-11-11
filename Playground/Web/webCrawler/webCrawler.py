import os
import re

import requests
from bs4 import BeautifulSoup


class Crawler():
    def __init__(self):
        print("Start")

    def google_url(self, find):
        return "https://www.google.pl?gws_rd=ssl#q={x}".format(x=find)

    def get_links_pages(self, URLs):
        if not isinstance(URLs, list):
            return self.get_links_pages_for_base(URLs)
        else:
            maps_list = []
            for baseURL in URLs:
                maps_list.append(self.get_links_pages_for_base(baseURL))
            return maps_list

    def get_links_pages_for_base(self, url):
        links_parent = self.get_links_page(url)
        map_ = map(self.get_links_page, links_parent)
        return list(map_)

    def get_links_page(self, link):
        links = []
        try:
            link = self.regex_links(link)
            print(link[0])
            response = requests.get(link[0]).text
            soup = BeautifulSoup(response)
            links = soup.find_all("a", href=True)
        except Exception as ex:
            print(ex)
        return self.regex_links(links)

    def regex_links(self, text):
        all = re.findall(r'(https?://\S+)', str(text))
        map_ = map(self.cleanLink, all)
        list_ = list(map_)
        return list_

    def cleanLink(self, link):
        if ('>' in link): link = link[:link.index('>')]
        return link.replace("\"", "")

    def tofile(self,list_):
        list_ = self.cleanList(list_)
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path+"\\links.txt",'w') as f:
            for line in list_:
                f.write(line.strip()+'\n')
                f.flush()
        print("Links saved: "+str(len(list_)))

    def cleanList(self,list_):
         list_ = str(list_).replace("[","").replace("]","")
         list_=list_.split(',')
         return list_

def main():
    bot = Crawler()
    googl = bot.google_url("Tomasz Dworowy")
    links_list = bot.get_links_pages(googl)
    links_list2 = bot.get_links_pages(links_list)
    links_list3 = bot.get_links_pages(links_list2)
    links_list4 = bot.get_links_pages(links_list3)

    bot.tofile(links_list4)

if __name__ == "__main__":
    main()
