import argparse
import webbrowser

from league_team import LeagueTeam
from league_player import LeaguePlayer

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("team-url",
                        help="NSE URL of the team to scout")

    return parser.parse_args()

def main():
    args = parse_args()
    
    team = LeagueTeam(vars(args)["team-url"])
    for player in team.players:
        webbrowser.open_new_tab(player.opgg_link)
        print("Real Name: {0}\nSummoner Name: {1}\nOP.GG: {2}\n\n".format(player.real_name,player.summoner_name,player.opgg_link))
 
main()