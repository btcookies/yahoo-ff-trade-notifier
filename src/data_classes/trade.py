from dataclasses import dataclass
from typing import Dict, List

from src.data_classes.player import Player
from src.enums import TradeIdentifiers
from src.utils.player_utils import format_players_string
from src.utils.trade_utils import get_give_up, get_team


@dataclass
class Trade:
    sender: str
    receiver: str
    sender_gives_up: List
    receiver_gives_up: List

    def __init__(self, raw_trade: Dict):
        self.sender = get_team(raw_trade, TradeIdentifiers.SENDER.value)
        self.receiver = get_team(raw_trade, TradeIdentifiers.RECEIVER.value)
        self.sender_gives_up = get_give_up(raw_trade, self.sender)
        self.receiver_gives_up = get_give_up(raw_trade, self.receiver)

    def to_message(self) -> str:

        sender_assets = format_players_string(self.sender_gives_up)
        receiver_assets = format_players_string(self.receiver_gives_up)

        message = (
            "🚨TRADE COMPLETED🚨\n"
            "\n"
            f"{self.sender} GIVES UP:\n"
            f"{sender_assets}"
            "\n"
            f"{self.receiver} GIVES UP:\n"
            f"{receiver_assets}"
        )

        return message
