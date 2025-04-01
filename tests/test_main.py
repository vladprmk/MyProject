import pytest
from src.main import add_task, list_tasks, tasks

def setup_function():
    # Очищення списку задач перед кожним тестом
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
