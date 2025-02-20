from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_data: str) -> str:
    """
    Возвращает строку с замаскированным номером.
    Для карт и счетов используйте разные типы маскировки.
    """
    rend_card_data = card_data.split(" ")
    digit_of_card_data = rend_card_data[-1]
    card_or_account = rend_card_data[:-1]
    if rend_card_data[0] != "Счёт":
        masked_number = get_mask_card_number(digit_of_card_data)
    else:
        masked_number = get_mask_account(digit_of_card_data)

    return f'{" ".join(card_or_account)} {masked_number}'


def get_date(date: str) -> str:
    """ Преобразует даты из формата ISO 8601 в формат DD.MM.YYYY"""
    if not "T" and "-" in date:
        raise ValueError("Некорректный формат даты или времени")
    time_part, date_part = date.split("T")
    try:
        year, month, day = map(int, time_part.split("-"))
    except ValueError:
        raise ValueError("Некорректный формат даты")
    if not (1 <= month <= 12):
        raise ValueError("Некорректный месяц")
    if not (1 <= day <= 31):
        raise ValueError("Некорректный день")
    if month in {4, 6, 9, 11} and day > 30:
        raise ValueError("Некорректный день для месяца с 30 днями")
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                raise ValueError("Некорректное количество дней для февраля високосного года")
        elif day > 28:
            raise ValueError ("Некорректное количество дней для февраля невисокосного года")

    return f"{day:02}.{month:02}.{year}"


if __name__ == "__main__":
    print(mask_account_card("Maestro card 1596837868705199"))
    print(mask_account_card("Счёт 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
