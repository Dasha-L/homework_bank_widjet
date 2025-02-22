import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "transactions, state, expected_filtered_transactions",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            [
                {"id": 41528829, "state": "NEW", "date": "2019-07-03T18:35:29.512364"},
                {"id": 935719570, "state": "PENDING", "date": "2018-06-30T02:08:58.425572"},
                {"id": 514226727, "state": "COMPLETED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 605064591, "state": "FAILED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [],
        ),
        ([], "CANCELED", []),
        ([], "", []),
    ],
)
def test_filter_by_state_correct(
    transactions: list[dict], state: str, expected_filtered_transactions: list[dict]
) -> None:
    """Параметризация тестов для различных возможных значений статуса state"""
    assert filter_by_state(transactions, state) == expected_filtered_transactions


@pytest.mark.parametrize(
    "transactions, reverse, sorted_transactions",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date_correct(transactions: list[dict], reverse: bool, sorted_transactions: list[dict]) -> None:
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания."""
    assert sort_by_date(transactions, reverse) == sorted_transactions


def test_sort_by_date_with_same_dates(transactions_with_same_dates: list[dict]) -> None:
    """Проверка корректности сортировки при одинаковых датах"""
    result = sort_by_date(transactions_with_same_dates, reverse=True)
    expected_result = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-01T00:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-01T00:00:00.000000"},
    ]
    assert result == expected_result, "Порядок словарей с одинаковыми датами изменился"


def test_sort_by_date_with_invalid_dates(transactions_with_invalid_dates: list[dict]) -> None:
    """Тест на работу функции с некорректными или нестандартными форматами дат."""
    with pytest.raises(ValueError):
        sort_by_date(transactions_with_invalid_dates)
