import logging
from logging.handlers import RotatingFileHandler

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define handlers
stream_handler = logging.StreamHandler()
rotating_file_handler = RotatingFileHandler(
    "log_api.log", maxBytes=100 * 1024 * 1024, backupCount=5
)

# Format logs
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

stream_handler.setFormatter(formatter)
rotating_file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(stream_handler)
logger.addHandler(rotating_file_handler)
