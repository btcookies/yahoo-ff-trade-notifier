from typing import Dict, List

from src.data_classes.player import Player
from src.enums import TradeIdentifiers, TradeObjectKeys


class InvalidTeamType(Exception):
    pass


def get_give_up(raw_trade: Dict, team_name: str) -> List[Player]:
    """Returns the list of players team_name is giving up as part of the trade

    Args:
        raw_trade (Dict): Raw trade object returned from yahoo_fantasy_api.League.transactions("trade", n)
        team_name (str): Name of fantasy team
    Returns:
        List[str]: List of player objects team_name is giving up as part of the trade
    """
    given_up = []
    count = raw_trade[TradeObjectKeys.PLAYER_LIST.value]["count"]
    players: List = list(raw_trade[TradeObjectKeys.PLAYER_LIST.value].values())[:count]
    for player in players:
        player_info: List[Dict] = player["player"][0]
        league_info: Dict = player["player"][1]["transaction_data"][0]

        if league_info["source_team_name"] == team_name:
            formatted_player = get_player_from_info(player_info)
            given_up.append(formatted_player)

    return given_up


def get_player_from_info(player_info: List[Dict]) -> Player:
    name, nfl_team, position = None, None, None

    for metadata in player_info:
        if "name" in metadata.keys():
            name = metadata["name"]["full"]
        if "editorial_team_abbr" in metadata.keys():
            nfl_team = metadata["editorial_team_abbr"]
        if "display_position" in metadata.keys():
            position = metadata["display_position"]

    return Player(name=name, nfl_team=nfl_team, position=position)


def get_team(raw_trade: Dict, team_type: TradeIdentifiers) -> str:
    if team_type == TradeIdentifiers.SENDER.value:
        return raw_trade[TradeObjectKeys.SENDER_NAME.value]
    if team_type == TradeIdentifiers.RECEIVER.value:
        return raw_trade[TradeObjectKeys.RECEIVER_NAME.value]

    raise InvalidTeamType(f"Team type {team_type} is invalid")
