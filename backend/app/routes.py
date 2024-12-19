from typing import Annotated

from app.backlog import load_backlog, save_backlog
from app.config import templates
from app.models import Config, Vote
from app.rules import apply_rule
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse

router = APIRouter()


@router.post("/setup", response_class=HTMLResponse)
async def setup(
    request: Request,
    num_players: Annotated[int, Form(...)],
    player_names: Annotated[str, Form(...)],
    rule: Annotated[str, Form(...)],
):
    config = Config(
        num_players=num_players, player_names=player_names.split(","), rule=rule
    )
    backlog = load_backlog()
    print(f"the backlog is {backlog['backlog']}")
    return templates.TemplateResponse(
        "game.html",
        {
            "request": request,
            "backlog": backlog["backlog"],
            "rule": rule,
            "players": config.player_names,
        },
    )


@router.get("/backlog", response_class=JSONResponse)
async def get_backlog():
    backlog = load_backlog()
    return {"backlog": backlog["backlog"]}


# Endpoint pour voter
@router.post("/vote", response_class=JSONResponse)
async def vote(vote: Vote):
    backlog = load_backlog()
    for task in backlog["backlog"]:
        if task["id"] == vote.task_id:
            if "votes" not in task:
                task["votes"] = {}
            if vote.player in task["votes"]:
                return {"error": "Ce joueur a déjà voté pour cette tâche"}
            task["votes"][vote.player] = vote.estimate
            save_backlog(backlog)
            return {"message": "Vote enregistré"}
    return {"error": "Tâche introuvable"}


# Endpoint pour valider les votes
@router.post("/validate", response_class=JSONResponse)
async def validate(task_id: str, rule: str):
    backlog = load_backlog()
    for task in backlog["backlog"]:
        if task["id"] == task_id:
            votes = task.get("votes", [])
            result = apply_rule(rule, votes)
            task["validated"] = result["validated"]
            task["estimate"] = result["estimate"]
            save_backlog(backlog)
            return result
    return {"error": "Tâche introuvable"}
