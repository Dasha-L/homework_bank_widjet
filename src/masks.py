def get_mask_card_number(card_number: int) -> str:
    """
    Принимает на вход номер карты в виде числа и возвращает маску номера
    по правилу XXXX XX** **** XXXX
    """
    card_number_str = str(card_number)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** ****{card_number_str[-4:]}"


def get_mask_account(account_name: str) -> str:
    """
    Принимает на вход номер счета в виде числа и возвращает маску номера
    по правилу **XXXX
    """
    return f"**{account_name[1:]}"


if __name__ == "__main__":
    print(get_mask_card_number(12345678910121314))
    print(get_mask_account("123456"))
