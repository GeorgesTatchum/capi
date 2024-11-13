from app.game import start_game
from app.models import Config


def test_start_game():
    config = Config(
        num_players=3, player_names=["Alice", "Bob", "Charlie"], rule="Strict"
    )
    backlog = [{"name": "Task 1"}, {"name": "Task 2"}]
    result = start_game(config, backlog)
    assert len(result) == 2
    assert all(task["estimate"] is not None for task in result)
