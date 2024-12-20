from app.config import templates
from app.routes import router
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi_socketio import SocketManager

app = FastAPI(
    title="Planning Poker API",
    description="API pour gérer une partie de Planning Poker.",
)
sio = SocketManager(app=app)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(router)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
