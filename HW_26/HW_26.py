"""
Домашнее задание № 26
Часть 1: Декоратор для валидации пароля
"""
from typing import Tuple, Callable
import csv
import os

print('Часть 1: Декоратор для валидации пароля')

def password_checker(func: Callable) -> Callable:
    """
    Декоратор для валидации пароля
    """
    def wrapper(password: str) -> Callable:
        errors = []
        if len(password) < 8:
            errors.append('\tПароль должен содержать не менее 8 символов')
        if not any(char.isdigit() for char in password):
            errors.append('\tПароль должен содержать хотя бы одну цифру')
        if not any(char.islower() for char in password if char.isalpha()):
            errors.append('\tПароль должен содержать хотя бы одну строчную букву')
        if not any(char.isupper() for char in password if char.isalpha()):
            errors.append('\tПароль должен содержать хотя бы одну заглавную букву')
        if not any(char in '.,;:!?_*-+()/#¤@%&)' for char in password):
            errors.append('\tПароль должен содержать хотя бы один спецсимвол')
        if errors:
            raise ValueError('\n'.join(errors))
        return func(password)
    return wrapper

@password_checker
def register_user(password: str) -> str:
    """
    Функция для регистрации пользователя
    """
    return f'Регистрация прошла успешно.'

try:
    print(register_user(input('Введите пароль: ')))
except ValueError as e:
    print(f'Ошибка регистрации:\n{e}')


"""
    mypy HW_26.py 
    *** Success: no issues found in 1 source file
"""

"""
Часть 2: Декораторы для валидации данных
"""

ACCESS_FILE = 'acl.csv'

print('Часть 2: Декораторы для валидации данных')

def create_logger(log_prefix: str) -> Callable:
    """
    Дополнительное замыкание (логирование операций) (опционально)
    """
    def log_registration() -> str:
        username: str = input(f'{log_prefix}: Введите логин: ')
        password: str = input(f'{log_prefix}: Введите пароль: ')
        print(f"{log_prefix}: Попытка регистрации пользователя {username}")
        result = register_user2(username, password)
        print(f"{log_prefix}: {result}")
        return result
    return log_registration

def password_validator(min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1, min_special_chars: int = 1) -> Callable:
    """
    **Параметры**:
        - `min_length`: Минимальная длина пароля (по умолчанию 8).
        - `min_uppercase`: Минимальное количество заглавных букв (по умолчанию 1).
        - `min_lowercase`: Минимальное количество строчных букв (по умолчанию 1).
        - `min_special_chars`: Минимальное количество специальных символов (по умолчанию 1).
    **Функциональность**:
        - Проверяет, соответствует ли пароль заданным критериям.
        - Если пароль не соответствует, выбрасывает `ValueError` с описанием проблемы.
    """
    def wrapper(func: Callable) -> Callable:
        def inner(username: str, password: str) -> Callable:
            errors = []
            if len(password) < min_length:
                errors.append(f'\tПароль должен содержать не менее {min_length} символов.')
            if [char.isupper() for char in password if char.isalpha()].count(True) < min_uppercase:
                errors.append(f'\tПароль должен содержать заглавные буквы в колличестве не менее: {min_uppercase} штук.')
            if [char.islower() for char in password if char.isalpha()].count(True) < min_lowercase:
                errors.append(f'\tПароль должен содержать строчные буквы в колличестве не менее: {min_lowercase} штук.')
            # Исключаем символ ":", так как он используется в csv файле для разделения полей
            if any(char == ':' for char in password):
                errors.append('\tПароль не должен содержать символ ":"')
            if [char in '.,;!?_*-+()/#¤%@&)' for char in password].count(True) < min_special_chars:
                errors.append(f'\tПароль должен содержать спецсимволы в колличестве не менее: {min_special_chars} штук.')
            if errors:
                raise ValueError('\n'.join(errors))
            return func(username, password)
        return inner
    return wrapper

def username_validator(func: Callable) -> Callable:
    """
    **Функциональность**:
        - Проверяет, что в имени пользователя отсутствуют пробелы.
        - Если в имени пользователя есть пробелы, выбрасывает `ValueError` с описанием проблемы.
    """
    def wrapper(username: str, password: str) -> Callable:
        errors = []
        # Исключаем символ ":", так как он используется в csv файле для разделения полей
        if any(char == ':' for char in username):
            errors.append('\tЛогин не должен содержать символ ":"')
        if [char for char in username].count(' ') > 0:
            errors.append('\tЛогин не должен содержать пробелы.')
        if errors:
            raise ValueError('\n'.join(errors))
        return(func(username, password))
    return wrapper

@username_validator
@password_validator(min_length=8, min_uppercase=1, min_lowercase=1, min_special_chars=1)
def register_user2(username: str, password: str) -> str:
    """
        - Принимает `username` и `password`.
        - **Функциональность**:
        - Дозаписывает имя пользователя и пароль в CSV файл.
        - Оборачивается обоими декораторами для валидации данных.
    """
    row: dict = {'username': username, 'password': password}
    with open(ACCESS_FILE, 'a', encoding = 'utf-8-sig', newline = "") as file:
        writer = csv.DictWriter(file, fieldnames=row.keys(), delimiter = ':')
        writer.writerow(row)
    return f'Регистрация прошла успешно.'

register_with_logging = create_logger("[REGISTRATION]")

try:
    register_with_logging()
except ValueError as e:
    print(f'Ошибка регистрации:\n{e}')

"""
    mypy HW_26.py
    *** Success: no issues found in 1 source file
"""