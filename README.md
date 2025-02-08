# Виджет для отображения последних успешных банковских операций

Этот проект представляет собой виджет для личного кабинета клиента, который отображает несколько последних успешных банковских операций. Виджет включает в себя функции для маскировки номеров карт и счетов, а также для фильтрации и сортировки транзакций по дате и статусу.

---

## Основные функции

### 1. Маскировка номеров карт и счетов
- **`get_mask_card_number(card_number: str) -> str`**  
  Принимает номер карты и возвращает его маску в формате `XXXX XX** **** XXXX`.  
  Пример:  
  ```python
  get_mask_card_number("1596837868705199")  # Возвращает "1596 83** **** 5199"
  ```

- **`get_mask_account(account_name: str) -> str`**  
  Принимает номер счёта и возвращает его маску в формате `**XXXX`.  
  Пример:  
  ```python
  get_mask_account("73654108430135874305")  # Возвращает "**4305"
  ```

- **`mask_account_card(card_data: str) -> str`**  
  Принимает строку с данными карты или счёта и возвращает её с замаскированным номером.  
  Пример:  
  ```python
  mask_account_card("Maestro card 1596837868705199")  # Возвращает "Maestro card 1596 83** **** 5199"
  mask_account_card("Счёт 73654108430135874305")      # Возвращает "Счёт **4305"
  ```

---

### 2. Преобразование даты
- **`get_date(date: str) -> str`**  
  Преобразует дату из формата ISO 8601 (`YYYY-MM-DDTHH:MM:SS.microseconds`) в формат `DD.MM.YYYY`.  
  Пример:  
  ```python
  get_date("2024-03-11T02:26:18.671407")  # Возвращает "11.03.2024"
  ```

---

### 3. Фильтрация и сортировка транзакций
- **`filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]`**  
  Фильтрует список транзакций по статусу выполнения (по умолчанию — `EXECUTED`).  
  Пример:  
  ```python
  transactions = [
      {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
  ]
  filter_by_state(transactions)  # Возвращает только транзакции со статусом 'EXECUTED'
  ```

- **`sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]`**  
  Сортирует список транзакций по дате. По умолчанию сортировка выполняется по убыванию (сначала самые последние операции).  
  Пример:  
  ```python
  sort_by_date(transactions)  # Возвращает транзакции, отсортированные по убыванию даты
  sort_by_date(transactions, reverse=False)  # Возвращает транзакции, отсортированные по возрастанию даты
  ```

---

## Как использовать

1. **Установка зависимостей**  
   Убедитесь, что у вас установлен Python 3.8 или выше. Дополнительные зависимости не требуются.

2. **Импорт функций**  
   Импортируйте необходимые функции из модулей `masks.py`, `widget.py` и `processing.py`.  
   Пример:  
   ```python
   from src.masks import get_mask_card_number, get_mask_account
   from src.widget import mask_account_card, get_date
   from src.processing import filter_by_state, sort_by_date
   ```

3. **Пример использования**  
   ```python
   # Маскировка номера карты
   masked_card = get_mask_card_number("1596837868705199")
   print(masked_card)  # Вывод: "1596 83** **** 5199"

   # Маскировка номера счёта
   masked_account = get_mask_account("73654108430135874305")
   print(masked_account)  # Вывод: "**4305"

   # Преобразование даты
   formatted_date = get_date("2024-03-11T02:26:18.671407")
   print(formatted_date)  # Вывод: "11.03.2024"

   # Фильтрация и сортировка транзакций
   transactions = [
       {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
   ]
   filtered_transactions = filter_by_state(transactions)
   sorted_transactions = sort_by_date(filtered_transactions)
   print(sorted_transactions)
   ```

---

## Структура проекта

```
project/
├── src/
│   ├── masks.py          # Функции для маскировки номеров карт и счетов
│   ├── widget.py         # Функции для работы с данными карт, счетов и дат
│   ├── processing.py     # Функции для фильтрации и сортировки транзакций
├── README.md             # Документация проекта
```

---

## Лицензия

Этот проект распространяется под лицензией MIT.

---

## Автор

Dasha-L
dl274274@hotmsil.com 
