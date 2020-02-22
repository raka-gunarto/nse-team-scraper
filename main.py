import argparse

from league_team import LeagueTeam

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("team-url",
                        help="NSE URL of the team to scout")

    return parser.parse_args()

def main():
    args = parse_args()
    
    team = LeagueTeam(vars(args)["team-url"])
 
main()