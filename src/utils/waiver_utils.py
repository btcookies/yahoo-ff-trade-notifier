from typing import Dict, List, Optional, Tuple

from src.data_classes.player import Player
from src.enums import WaiverObjectKeys
from src.utils.player_utils import get_player_from_info


class InvalidWaiverClaim(Exception):
    pass


def get_waiver_txs(raw_waiver: Dict) -> Tuple[List[Player]]:
    adds = []
    drops = []

    count = raw_waiver["players"]["count"]
    players: List = list(raw_waiver["players"].values())[:count]

    for player in players:
        player_info: List[Dict] = player["player"][0]
        formatted_player = get_player_from_info(player_info)

        if type(player["player"][1]["transaction_data"]) == list:
            league_info: Dict = player["player"][1]["transaction_data"][0]
        else:
            league_info: Dict = player["player"][1]["transaction_data"]

        if league_info["type"] == WaiverObjectKeys.ADD.value:
            adds.append(formatted_player)
        if league_info["type"] == WaiverObjectKeys.DROP.value:
            drops.append(formatted_player)

    return adds, drops


def get_team(raw_waiver: Dict) -> str:
    if type(raw_waiver["players"]["0"]["player"][1]["transaction_data"]) == list:
        metadata = raw_waiver["players"]["0"]["player"][1]["transaction_data"][0]
    else:
        metadata = raw_waiver["players"]["0"]["player"][1]["transaction_data"]

    if WaiverObjectKeys.DESTINATION_TEAM.value in metadata.keys():
        return metadata[WaiverObjectKeys.DESTINATION_TEAM.value]
    if WaiverObjectKeys.SOURCE_TEAM.value in metadata.keys():
        return metadata[WaiverObjectKeys.SOURCE_TEAM.value]

    raise InvalidWaiverClaim("Raw waiver object missing team name")
