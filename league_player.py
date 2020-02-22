from bs4 import BeautifulSoup
import urllib.request

import logging

OP_GG_BASE_URL = "https://euw.op.gg/summoner/userName="

class LeaguePlayer:
    def __init__(self, url):
        self.html_soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")
        self.real_name = self.html_soup.find("h1", class_="university-title").decode_contents().replace('\n','').strip()
        self.summoner_name = ""

        self.opgg_link = self.__get_opgg().replace(" ","%20")
        self.opgg_soup = BeautifulSoup(urllib.request.urlopen(self.opgg_link).read(), features="html.parser")

    def __get_opgg(self):
        for div in self.html_soup.findAll("div"):
            try:
                label = div.findAll("div")[0].decode_contents()
                if label == "Summoner Name":
                    self.summoner_name = div.findAll("div")[1].decode_contents()
                    return OP_GG_BASE_URL + div.findAll("div")[1].decode_contents()
            except:
                pass
        
        logging.warn("Unable to find summoner name for player %s", self.real_name)