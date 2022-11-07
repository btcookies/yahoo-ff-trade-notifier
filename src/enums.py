from enum import Enum


class TradeIdentifiers(Enum):
    SENDER = "sender"
    RECEIVER = "receiver"


class TradeObjectKeys(Enum):
    SENDER_NAME = "trader_team_name"
    RECEIVER_NAME = "tradee_team_name"
    PLAYER_LIST = "players"


class WaiverObjectKeys(Enum):
    SOURCE_TEAM = "source_team_name"
    DESTINATION_TEAM = "destination_team_name"
    PLAYER_LIST = "players"
    ADD = "add"
    DROP = "drop"
