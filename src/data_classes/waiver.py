from dataclasses import dataclass
from typing import Dict, List

from src.data_classes.player import Player
from src.utils.player_utils import format_players_string
from src.utils.waiver_utils import get_team, get_waiver_txs


@dataclass
class Waiver:
    team: str
    adds: List
    drops: List

    def __init__(self, raw_waiver: Dict):
        self.team = get_team(raw_waiver)
        self.adds, self.drops = get_waiver_txs(raw_waiver)

    def to_message(self) -> str:

        add_assets = None if self.adds == [] else format_players_string(self.adds)
        drop_assets = None if self.drops == [] else format_players_string(self.drops)

        message = f"{self.team} "

        if add_assets:
            message += f"ADDS:\n{add_assets}"
        if drop_assets:
            message += f"DROPS:\n{drop_assets}"

        return message
