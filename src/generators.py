def filter_by_currency(transactions_list, currency):
    """Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной."""

    def is_currency_match(item):
        operation_amount = item.get("operationAmount")
        if not isinstance(operation_amount, dict):
            return False
        currency_data = operation_amount.get("currency")
        if not isinstance(currency_data, dict):
            return False
        return currency_data.get("code") == currency

    for transaction in transactions_list:
        if is_currency_match(transaction):
            yield transaction


def transaction_descriptions(transactions_list):
    """Возвращает описание каждой транзакции по очереди"""
    for trans in transactions_list:
        yield f"{trans['description']}"


def card_number_generator(start, stop):
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    cards_numbers = []
    for number in range(start, stop + 1):
        if 0 <= number <= 9999999999999999:
            card_number_str = f"{number:016}"
            formatted_card = (
                f"{card_number_str[:4]} {card_number_str[4:8]} {card_number_str[8:12]} {card_number_str[12:]}"
            )
            cards_numbers.append(formatted_card)
    return cards_numbers
