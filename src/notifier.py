import json
import os

from dataclasses import dataclass
from typing import Dict, List

from yahoo_fantasy_api import Game, League
from yahoo_oauth import OAuth2

from src.data_classes.trade import Trade
from src.data_classes.waiver import Waiver

MAX_TXS = 500
AUTH_FILE_PATH = "./src/auth.json"


if "__main__" == __name__:

    oauth = OAuth2(None, None, from_file=AUTH_FILE_PATH)
    league_ids = Game(oauth, "nfl").league_ids()

    for _id in league_ids:
        print(_id)

    league = League(oauth, league_ids[0])
    waivers = league.transactions("add", MAX_TXS)
    drops = league.transactions("drop", MAX_TXS)
    raw_trades = league.transactions("trade", MAX_TXS)

    formatted_trades = []
    for raw_trade in raw_trades:
        formatted_trade = Trade(raw_trade)
        formatted_trades.append(formatted_trade)

    for t in formatted_trades:
        print(t.to_message())

    # print(json.dumps(adds[5], indent=4))
    # print(len(adds))
    formatted_waivers = []

    for w in waivers:
        formatted_waiver = Waiver(w)
        formatted_waivers.append(formatted_waiver)

    waiver_message = "✅WAIVER CLAIMS COMPLETED✅\n\n"
    for w in formatted_waivers:
        waiver_message += w.to_message() + "\n"
    print(waiver_message)
