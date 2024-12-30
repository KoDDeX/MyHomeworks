"""
Домашнее задание № 26
Часть 1: Декоратор для валидации пароля
"""

from typing import Any, Dict, Tuple, List, Callable


def password_checker(func: Callable) -> Callable:
    """
    Декоратор для валидации пароля
    """
    def wrapper(password: str) -> Callable:
        if len(password) < 8:
            raise ValueError('Пароль должен содержать не менее 8 символов')
        if not any(char.isdigit() for char in password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not any(char.isalpha() for char in password):
            raise ValueError('Пароль должен содержать хотя бы одну строчную букву')
        if not any(char.isupper() for char in password if char.isalpha()):
            raise ValueError('Пароль должен содержать хотя бы одну заглавную букву')
        if not any(char in '.,:;!_*-+()/#¤%&)' for char in password):
            raise ValueError('Пароль должен содержать хотя бы один спецсимвол')
        return func(password)
    return wrapper

@password_checker
def register_user(password: str) -> None:
    """
    Функция для регистрации пользователя
    """
    pass
    return f'Регистрация прошла успешно.'

print(register_user(input('Введите пароль: ')))