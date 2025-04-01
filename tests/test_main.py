import sys
import os
import builtins
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import add_task, list_tasks, tasks

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

def test_main_flow(monkeypatch, capsys):
    # Емуляція користувача: додати завдання, показати список, вийти
    inputs = iter(["1", "Do homework", "2", "3"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Запускаємо файл src/main.py як скрипт
    main_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/main.py'))
    with open(main_path, encoding='utf-8') as f:
        code = f.read()
    exec(compile(code, main_path, 'exec'))

    out = capsys.readouterr().out
    assert "Task 'Do homework' added." in out
    assert "1. Do homework" in out
