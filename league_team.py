from bs4 import BeautifulSoup
import urllib.request

from league_player import LeaguePlayer

BASE_URL = "https://tournaments.nse.gg/"

class LeagueTeam:
    def __init__(self, url):
        self.html_soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")
        self.__parse_players()

    def __parse_players(self):
        self.players = []

        player_rows = self.html_soup.find("table", class_="table-players").findAll("tr")
        for i in range(1, len(player_rows)):
            player_row = player_rows[i]
            url_path = player_row.find('a')["href"]

            self.players.append(LeaguePlayer((BASE_URL + url_path).replace(" ","%20")))
