from src.widget import get_date
from datetime import datetime


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """" Фильтрует список транзакций по статусу выполнения"""
    return [t for t in transactions if t["state"] == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список транзакций по дате."""

    def convert_date(d: dict) -> datetime:
        """Преобразует дату из словаря в объект datetime для сортировки."""
        date_str = get_date(d["date"])
        return datetime.strptime(date_str, "%d.%m.%Y")

    return sorted(transactions, key=convert_date, reverse=reverse)


if __name__ == "__main__":
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(filter_by_state(transactions))
    print(sort_by_date(transactions))
