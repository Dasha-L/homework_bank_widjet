from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_data: str) -> str:
    rend_card_data = card_data.split(" ")
    digit_of_card_data = rend_card_data[-1]
    card_or_account = rend_card_data[:-1]
    if len(digit_of_card_data) == 16:
        masked_number = get_mask_card_number(digit_of_card_data)
    else:
        masked_number = get_mask_account(digit_of_card_data)

    return f'{" ".join(card_or_account)} {masked_number}'


# def get_date(date:str) -> str:
# return correct_date(date[0:10])

if __name__ == '__main__':
    print(mask_account_card("Maestro card 1596837868705199"))
    print(mask_account_card("Счёт 73654108430135874305"))
    # print(get_date("2024-03-11T02:26:18.671407"))
