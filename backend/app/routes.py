from app.backlog import load_backlog, save_backlog
from app.game import start_game
from app.main import sio
from app.models import Config
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.post("/setup", response_class=HTMLResponse)
async def setup(
    request: Request,
    num_players: int = Form(...),
    player_names: str = Form(...),
    rule: str = Form(...),
):
    config = Config(
        num_players=num_players, player_names=player_names.split(","), rule=rule
    )
    backlog = load_backlog()
    result = start_game(config, backlog)
    save_backlog(result)
    return templates.TemplateResponse(
        "game.html", {"request": request, "backlog": result}
    )


@sio.on("vote")
async def handle_vote(sid, data):
    # Handle vote logic here
    pass


@sio.on("connect")
async def handle_connect(sid, environ):
    print("Client connected:", sid)


@sio.on("disconnect")
async def handle_disconnect(sid):
    print("Client disconnected:", sid)
