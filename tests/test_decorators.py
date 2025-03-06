import pytest  # noqa: F401

from src.decorators import log


def test_log_to_file():
    """Тест логирования в файл."""

    @log(filename="test_log.txt")
    def add(a, b):
        return a + b

    add(1, 2)
    with open("test_log.txt", "r") as f:
        assert "add ok" in f.read()

    import os

    os.remove("test_log.txt")


def test_log_to_console(capsys):
    """Тест логирования в консоль."""

    @log()
    def add(a, b):
        return a + b

    add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out

    try:
        add(1, "2")
    except TypeError:
        pass
    captured = capsys.readouterr()
    assert "add error" in captured.out


def test_log_error():
    """Тест логирования ошибки."""

    @log(filename="test_error_log.txt")
    def divide(a, b):
        return a / b

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    with open("test_error_log.txt", "r") as f:
        assert "divide error" in f.read()

    import os

    os.remove("test_error_log.txt")
