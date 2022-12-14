import json

from src.data_classes.player import Player
from src.data_classes.trade import Trade
from src.utils.trade_utils import get_give_up, get_player_from_info

TEST_PLAYER_INFO = [
    {"player_key": "380.p.26561"},
    {"player_id": "26561"},
    {
        "name": {
            "full": "Josh Gordon",
            "first": "Josh",
            "last": "Gordon",
            "ascii_first": "Josh",
            "ascii_last": "Gordon",
        }
    },
    {"editorial_team_abbr": "Ten"},
    {"display_position": "WR"},
    {"position_type": "O"},
]

EXPECTED_TRADE_MESSAGE = """🚨TRADE COMPLETED🚨

JUULio Jones GIVES UP:
- Jarvis Landry, NO WR
- Greg Olsen, SEA TE

Slap Dick Bandits GIVES UP:
- Josh Gordon, TEN WR
"""


def test_get_give_up():
    with open("tests/data/trade.json") as f:
        trade = json.load(f)
    team_name = "JUULio Jones"
    given_up = get_give_up(trade, team_name)

    assert given_up == [
        Player(name="Jarvis Landry", nfl_team="NO", position="WR"),
        Player(name="Greg Olsen", nfl_team="Sea", position="TE"),
    ]


def test_get_player_from_info():
    player = get_player_from_info(TEST_PLAYER_INFO)

    assert player == Player(name="Josh Gordon", nfl_team="Ten", position="WR")


def test_trade_message():
    with open("tests/data/trade.json") as f:
        raw_trade = json.load(f)

    example = Trade(raw_trade)

    assert example.to_message() == EXPECTED_TRADE_MESSAGE
