from dataclasses import dataclass
from typing import Dict, List

from src.enums import TradeIdentifiers
from src.trade_utils import get_give_up, get_team


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