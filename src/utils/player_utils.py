from typing import Dict, List

from src.data_classes.player import Player


def format_players_string(assets: List[Player]) -> str:
    indent = "- "
    assets_str = ""

    for asset in assets:
        assets_str += (
            indent
            + f"{asset.name}, {asset.nfl_team.upper()} {asset.position.upper()}"
            + "\n"
        )

    return assets_str


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
