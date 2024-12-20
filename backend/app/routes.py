from typing import Annotated

from app.backlog import load_backlog, save_backlog
from app.config import templates
from app.models import Config, Vote
from app.rules import apply_rule
from fastapi import APIRouter, Body, Form, Request
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
        num_players=num_players, player_names=player_names.split(","), rule=rule.lower()
    )
    backlog = load_backlog()
    active_tasks = [task for task in backlog.backlog if not task.validated]
    return templates.TemplateResponse(
        "game.html",
        {
            "request": request,
            "backlog": active_tasks,
            "rule": rule,
            "players": config.player_names,
        },
    )


@router.get("/backlog", response_class=JSONResponse)
async def get_backlog():
    backlog = load_backlog()
    # active_tasks = [task for task in backlog.backlog if not task.validated]
    return {"backlog": backlog.backlog}


# Endpoint pour voter
@router.post("/vote", response_class=JSONResponse)
async def vote(vote: Vote):
    backlog = load_backlog()
    for task in backlog.backlog:
        if task.id == vote.task_id and not task.validated:
            if vote.player in task.votes:
                return {"error": "Ce joueur a déjà voté pour cette tâche"}
            task.votes[vote.player] = vote.estimate
            save_backlog(backlog)
            return {"message": "Vote enregistré"}
    return {"error": "Tâche introuvable ou déjà validée"}


# Endpoint pour valider les votes
@router.post("/validate", response_class=JSONResponse)
async def validate(task_id: str = Body(...), rule: str = Body(...)):
    backlog = load_backlog()
    for task in backlog.backlog:
        if task.id == task_id and not task.validated:
            votes = list(task.votes.values())
            # au cas où on n'est pas au second tour, on utilise la règle stricte
            if (rule != "strict" and task.step == 0) or rule == "strict":
                result = apply_rule(votes)
            else:
                result = apply_rule(votes, rule)

            if result["validated"] == False:
                task.votes = {}

            task.validated = result["validated"]
            task.estimatedPoints = result["estimate"]
            task.step += 1
            save_backlog(backlog)
            return result
    return {"error": "Tâche introuvable ou déjà validée"}
