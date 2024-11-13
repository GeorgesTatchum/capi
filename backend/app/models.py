from typing import List

from pydantic import BaseModel


class Config(BaseModel):
    num_players: int
    player_names: List[str]
    rule: str
