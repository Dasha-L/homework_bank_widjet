Дополним ваш `README.md` информацией о новом модуле `decorators` и его тестами. Вот обновленный текст:

---

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
│   ├── generators.py     # Функции для работы с транзакциями и генерации номеров карт
│   ├── decorators.py     # Декораторы для логирования
├── tests/
│   ├── test_masks.py     # Тесты для функций маскировки
│   ├── test_widget.py    # Тесты для функций работы с данными карт, счетов и дат
│   ├── test_processing.py # Тесты для функций фильтрации и сортировки транзакций
│   ├── test_generators.py # Тесты для функций модуля generators
│   ├── test_decorators.py # Тесты для декораторов
├── README.md             # Документация проекта
```

---

## Модуль decorators

Модуль `decorators` содержит декораторы для логирования выполнения функций.

### Декоратор `log`

Декоратор `log` автоматически логирует начало и конец выполнения функции, а также её результаты или возникшие ошибки. Логи могут записываться в файл или выводиться в консоль.

#### Параметры:
- **`filename` (str, optional):** Имя файла для записи логов. Если не указано, логи выводятся в консоль.

#### Пример использования:
```python
from src.decorators import log

@log(filename="mylog.txt")
def add(a, b):
    return a + b

add(1, 2)  # Логи записываются в файл mylog.txt
```

#### Ожидаемый вывод в файл `mylog.txt` при успешном выполнении:
```
add ok
```

#### Ожидаемый вывод при ошибке:
```
add error: TypeError. Inputs: (1, "2"), {}
```

---

## Тестирование

### Модуль decorators.py

#### Декоратор `log`
- **Тест логирования в файл:**
  - Проверяет, что логи записываются в указанный файл при успешном выполнении функции.
  - Проверяет, что логи записываются в файл при возникновении ошибки.

- **Тест логирования в консоль:**
  - Проверяет, что логи выводятся в консоль при успешном выполнении функции.
  - Проверяет, что логи выводятся в консоль при возникновении ошибки.

- **Тест обработки ошибок:**
  - Проверяет, что декоратор корректно логирует тип ошибки и входные параметры.

#### Пример теста:
```python
import pytest
from src.decorators import log

def test_log_to_file():
    @log(filename="test_log.txt")
    def add(a, b):
        return a + b

    add(1, 2)
    with open("test_log.txt", "r") as f:
        assert "add ok" in f.read()

    import os
    os.remove("test_log.txt")

def test_log_to_console(capsys):
    @log()
    def add(a, b):
        return a + b

    add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out

    try:
        add(1, "2")
    except TypeError:
        pass
    captured = capsys.readouterr()
    assert "add error" in captured.out
```

---

## Лицензия

Этот проект распространяется под лицензией MIT.

---

## Автор

- **Имя:** Dasha-L  
- **Email:** dl274274@hotmail.com
- 