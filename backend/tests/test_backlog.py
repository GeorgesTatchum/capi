from backend.app.backlog import load_backlog


def test_load_backlog():
    backlog = load_backlog()
    assert backlog


def test_save_backlog():
    pass
