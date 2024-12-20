from typing import Dict, List, Optional

from pydantic import BaseModel


class Task(BaseModel):
    id: str
    title: str
    description: str
    estimatedPoints: Optional[int] = None
    votes: Dict[str, int] = {}
    validated: bool = False
    step: int = 0


class Backlog(BaseModel):
    project: str
    sprint: str
    backlog: List[Task]


class Config(BaseModel):
    num_players: int
    player_names: List[str]
    rule: str


class Vote(BaseModel):
    task_id: str
    player: str
    estimate: int
