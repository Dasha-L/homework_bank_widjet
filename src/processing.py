from datetime import datetime

from src.widget import get_date


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ " Фильтрует список транзакций по статусу выполнения"""
    return [t for t in transactions if t["state"] == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список транзакций по дате."""

    def convert_date(d: dict) -> datetime:
        """Преобразует дату из словаря в объект datetime для сортировки."""
        date_str = get_date(d["date"])
        return datetime.strptime(date_str, "%d.%m.%Y")

    return sorted(transactions, key=convert_date, reverse=reverse)
