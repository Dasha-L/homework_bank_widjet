import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid(valid_card_numbers: list[str], expected_mask_numbers: list[str]) -> None:
    """Тестирование правильности маскирования номера карты."""
    for card_number, expected_mask_number in zip(valid_card_numbers, expected_mask_numbers):
        assert get_mask_card_number(card_number) == expected_mask_number


def test_get_mask_card_number_invalid(invalid_card_numbers: list[str]) -> None:
    """Проверка работы функции на различных входных форматах номеров карт,
    включая граничные случаи и нестандартные длины номеров, а также
    входные строки, где отсутствует номер карты."""
    for card_number in invalid_card_numbers:
        with pytest.raises(ValueError):
            get_mask_card_number(card_number)


def test_get_mask_account_valid(valid_account_numbers: list[str], expected_mask_accounts: list[str]) -> None:
    """Тестирование правильности маскирования номера счёта."""
    for valid_account_number, expected_mask_account in zip(valid_account_numbers, expected_mask_accounts):
        assert get_mask_account(valid_account_number) == expected_mask_account


def test_get_mask_account_invalid(invalid_account_numbers: list[str]) -> None:
    """Проверка работы функции с различными форматами и длинами номеров счетов и
    функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины."""
    for invalid_account_number in invalid_account_numbers:
        with pytest.raises(ValueError):
            get_mask_account(invalid_account_number)
