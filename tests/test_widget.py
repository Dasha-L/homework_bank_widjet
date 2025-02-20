import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "acc_card, mask_acc_card_result",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** ****3456"),  # Номер карты 16 цифр
        ("Maestro 9876544443210987654", "Maestro 9876 54** ****7654"),  # Номер карты 19 цифр
        ("Maestro card 1596835705199", "Maestro card 1596 83** ****5199"),
        # Наименование карты из двух слов, номер 13 цифр
        ("Счёт 874305", "Счёт **4305"),  # Счёт 6 цифр
        ("Счёт 98765432109876547676", "Счёт **7676"),  # Счёт 20 цифр
    ]
)
def test_mask_account_card_valid(acc_card, mask_acc_card_result):
    """ Параметризованный тесты с разными типами карт и счетов для проверки универсальности функции."""
    assert mask_account_card(acc_card) == mask_acc_card_result


# Параметризация для невалидных данных
@pytest.mark.parametrize(
    "invalid_acc_card",
    [
        "Visa 12345",  # Номер карты длиной 5 цифр
        "Счёт 123",  # Номер счета длиной 3 цифры
        "МИР 1234abcd5678",  # Номер карты с буквами
        "Счёт 1234!@#$",  # Номер счета с символами
        "Naster Card 1234 5678 9012 3456",  # Номер карты с пробелами
        "Счёт ",  # Пустой номер счета
    ],
)
def test_mask_account_card_invalid(invalid_acc_card):
    """Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам."""
    with pytest.raises(ValueError):
        mask_account_card(invalid_acc_card)


@pytest.mark.parametrize(
    "input_iso_date, expected_date_result",
    [
        ("2023-10-05T12:34:56", "05.10.2023"),  # Стандартная дата
        ("1999-01-01T00:00:00", "01.01.1999"),  # Граничный случай (начало года)
        ("2100-12-31T23:59:59", "31.12.2100"),  # Граничный случай (конец года)
        ("2000-02-29T12:00:00", "29.02.2000"),  # Високосный год
        ("2025-02-19T00:00:00", "19.02.2025"),  # Текущая дата (на момент написания теста)
    ]
)
def test_get_date_valid(input_iso_date, expected_date_result):
    """Тестирование правильности преобразования даты, включая граничные случаи и нестандартные строки с датами."""
    assert get_date(input_iso_date) == expected_date_result


def test_get_date_invalid(invalid_dates):
    """ Проверка работы функции на различных входных форматах даты,
        а также, что функция корректно обрабатывает входные строки, где отсутствует дата"""
    for invalid_date in invalid_dates:
        with pytest.raises(ValueError):
            get_date(invalid_date)
