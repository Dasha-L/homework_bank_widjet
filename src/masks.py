def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает маску номера
    по правилу XXXX XX** **** XXXX
    """

    return f"{card_number[:4]} {card_number[4:6]}** ****{card_number[-4:]}"


def get_mask_account(account_name: str) -> str:
    """
    Принимает на вход номер счета и возвращает маску номера
    по правилу **XXXX
    """
    return f"**{account_name[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("1596837868705199"))
    print(get_mask_account("73654108430135874305"))
