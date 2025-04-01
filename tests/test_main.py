from src.main import add_task, delete_task

def test_add_task(monkeypatch):
    tasks = []
    monkeypatch.setattr("builtins.input", lambda _: "Test Task")
    add_task(tasks)
    assert tasks == ["Test Task"]

def test_delete_task(monkeypatch):
    tasks = ["Task 1", "Task 2"]
    monkeypatch.setattr("builtins.input", lambda _: "1")
    delete_task(tasks)
    assert tasks == ["Task 2"]
