def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты от 13 до 19 символов и возвращает маску номера
    по правилу XXXX XX** **** XXXX
    """
    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")
    if len(card_number) < 13 or len(card_number) > 19:
        raise ValueError(
            f"Номер карты должен быть длиной от 13 до 19 символов," f" передан номер длиной {len(card_number)}"
        )
    else:
        return f"{card_number[:4]} {card_number[4:6]}** ****{card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Принимает на вход номер счета и возвращает маску номера
    по правилу **XXXX
    """
    if not account_number.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры")
    if len(account_number) < 6:
        raise ValueError(
            f"Номер счета должен быть длиной от 6 символов," f" передан номер длиной {len(account_number)}"
        )
    else:
        return f"**{account_number[-4:]}"
