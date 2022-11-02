import json
import os

from dataclasses import dataclass
from typing import Dict, List

from yahoo_fantasy_api import Game, League
from yahoo_oauth import OAuth2

from src.data_classes.trade import Trade

MAX_TXS = 50
AUTH_FILE_PATH = "./src/auth.json"



if "__main__" == __name__:

    oauth = OAuth2(None, None, from_file=AUTH_FILE_PATH)
    league_ids = Game(oauth, "nfl").league_ids()

    for _id in league_ids:
        print(_id)

    league = League(oauth, league_ids[0])
    adds = league.transactions("add", MAX_TXS)
    drops = league.transactions("drop", MAX_TXS)
    raw_trades = league.transactions("trade", MAX_TXS)

    # print(json.dumps(raw_trades[0], indent=4))

    formatted_trades = []
    for raw_trade in raw_trades:
        formatted_trade = Trade(raw_trade)
        formatted_trades.append(formatted_trade)

    for t in formatted_trades:
        print(t)
