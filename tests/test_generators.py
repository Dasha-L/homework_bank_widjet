import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

trans_list = [
    (
        [
            {"operationAmount": {"currency": {"code": "USD"}}},
            {"operationAmount": {"currency": {"code": "EUR"}}},
            {"operationAmount": {"currency": {"code": "USD"}}},
        ],
        "USD",
        [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}],
        "Тест 1: Корректная фильтрация по валюте 'USD'",
    ),
    (
        [{"operationAmount": {"currency": {"code": "EUR"}}}, {"operationAmount": {"currency": {"code": "GBP"}}}],
        "USD",
        [],
        "Тест 2: Нет транзакций в валюте 'USD'",
    ),
    ([], "USD", [], "Тест 3: Пустой список транзакций"),
    (
        [{"id": 1, "description": "Payment"}, {"id": 2, "description": "Withdrawal"}],
        "USD",
        [],
        "Тест 4: Список транзакций без валютных операций",
    ),
    (
        [
            {"operationAmount": {"currency": {"code": "USD"}}},
            {"id": 1, "description": "Payment"},
            {"operationAmount": {"currency": {"code": "USD"}}},
        ],
        "USD",
        [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}],
        "Тест 5: Неправильная структура данных (нет operationAmount)",
    ),
    (
        [{"operationAmount": "USD"}, {"operationAmount": "EUR"}, {"operationAmount": "USD"}],
        "USD",
        [],
        "Тест 6: Неправильный формат валюты (строка вместо словаря)",
    ),
    (
        [{"operationAmount": {"currency": {"code": "RUB"}}}, {"operationAmount": {"currency": {"code": "RUB"}}}],
        "RUB",
        [{"operationAmount": {"currency": {"code": "RUB"}}}, {"operationAmount": {"currency": {"code": "RUB"}}}],
        "Тест 7: Фильтрация по другой валюте 'RUB'",
    ),
    (
        [{"operationAmount": {"code": "USD"}}, {"operationAmount": {"code": "EUR"}}],
        "USD",
        [],
        "Тест 8: Отсутствие ключа 'currency'",
    ),
    (
        [{"id": 1, "description": "Payment"}, {"id": 2, "description": "Withdrawal"}],
        "USD",
        [],
        "Тест 9: Отсутствие ключа 'operationAmount'",
    ),
]


@pytest.mark.parametrize("transactions, currency, expected, test_description", trans_list)
def test_filter_by_currency(transactions, currency, expected, test_description):
    """Тесты проверяют:
    - что функция корректно фильтрует транзакции по заданной валюте;
    - правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют;
    - не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций.
    """
    result = list(filter_by_currency(transactions, currency))
    assert result == expected, f"Ошибка в тесте: {test_description}"


# Тест функции transaction_descriptions
def test_transaction_descriptions(trans_with_valid_descriptions, expected_trans_with_valid_descriptions):
    """Тест работы функции с различным количеством входных транзакций, включая пустой список."""
    for transactions, expected in zip(trans_with_valid_descriptions, expected_trans_with_valid_descriptions):
        assert list(transaction_descriptions(transactions)) == expected


test_card_numbers = [
    (
        1000,
        1005,
        [
            "0000 0000 0000 1000",
            "0000 0000 0000 1001",
            "0000 0000 0000 1002",
            "0000 0000 0000 1003",
            "0000 0000 0000 1004",
            "0000 0000 0000 1005",
        ],
        "Тест 1: Корректная генерация номеров карт в диапазоне",
    ),
    (0, 1, ["0000 0000 0000 0000", "0000 0000 0000 0001"], "Тест 2: Крайние значения диапазона"),
    (9999, 9999, ["0000 0000 0000 9999"], "Тест 3: Диапазон с одним значением"),
    (1005, 1000, [], "Тест 4: Некорректный диапазон (start > stop)"),
    (-10, -5, [], "Тест 5: Отрицательные значения"),
    (
        9999999999999990,
        9999999999999999,
        [
            "9999 9999 9999 9990",
            "9999 9999 9999 9991",
            "9999 9999 9999 9992",
            "9999 9999 9999 9993",
            "9999 9999 9999 9994",
            "9999 9999 9999 9995",
            "9999 9999 9999 9996",
            "9999 9999 9999 9997",
            "9999 9999 9999 9998",
            "9999 9999 9999 9999",
        ],
        "Тест 6: Большие значения (граничные случаи)",
    ),
]


@pytest.mark.parametrize("start, stop, expected, test_description", test_card_numbers)
def test_card_number_generator(start, stop, expected, test_description):
    """Тесты проверяют:
    - корректность генерации номеров карт в заданном диапазоне;
    - правильность форматирования номеров карт;
    - обработку крайних значений диапазона;
    - корректное завершение генерации.
    """
    result = card_number_generator(start, stop)
    assert result == expected, f"Ошибка в тесте: {test_description}"
