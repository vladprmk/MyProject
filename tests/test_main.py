import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import add_task, list_tasks, delete_task, tasks, get_task_count, get_sorted_tasks

# Setup that runs before each test
def setup_function():
    tasks.clear()

def test_add_valid_task():
    add_task("Read book")
    assert tasks == ["Read book"]

def test_add_task_with_whitespace():
    add_task("   Buy milk   ")
    assert tasks == ["Buy milk"]

def test_add_empty_task(capsys):
    add_task("   ")
    captured = capsys.readouterr()
    assert "cannot be empty" in captured.out
    assert tasks == []

def test_add_short_task(capsys):
    add_task("Go")
    captured = capsys.readouterr()
    assert "at least 3 characters" in captured.out
    assert tasks == []

def test_list_tasks_output(capsys):
    add_task("Task 1")
    add_task("Task 2")
    list_tasks()
    captured = capsys.readouterr()
    assert "1. Task 1" in captured.out
    assert "2. Task 2" in captured.out

def test_list_tasks_empty(capsys):
    list_tasks()
    captured = capsys.readouterr()
    assert "No tasks available." in captured.out

def test_delete_existing_task(capsys):
    add_task("Clean room")
    delete_task(1)
    captured = capsys.readouterr()
    assert "deleted" in captured.out
    assert tasks == []

def test_delete_invalid_index(capsys):
    add_task("Task X")
    delete_task(5)
    captured = capsys.readouterr()
    assert "Invalid task number" in captured.out
    assert tasks == ["Task X"]

def test_get_task_count():
    assert get_task_count() == 0
    add_task("Wash dishes")
    assert get_task_count() == 1

def test_get_sorted_tasks():
    add_task("Write report")
    add_task("Attend meeting")
    add_task("Buy coffee")
    result = get_sorted_tasks()
    assert result == ["Attend meeting", "Buy coffee", "Write report"]
