"""
Домашнее задание №23

Создание погодного приложения на Python.
"""

import requests
from plyer import notification

API_KEY = r"167349a6d42610462c6f5bd91a7c2e36"
CITY = "Обнинск"


def get_weather(city: str, api_key: str) -> dict:
    """
    Выполняет запрос к API и возвращает данные о погоде в виде словаря.
    """
    url = rf"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    return response.json()


def format_weather_message(weather_dict: dict) -> str:
    """
    Форматирует данные о погоде в удобочитаемое сообщение.
    """
    return f'Температура: {round(weather_dict["main"]["temp"])}°C\nОщущается как: {round(weather_dict["main"]["feels_like"])}°C\nОписание: {weather_dict["weather"][0]["description"]}'


def notify_weather(message: str) -> None:
    """
    Отправляет уведомление пользователю с информацией о погоде.
    """
    notification.notify(
        title=f"Погода в городе: {CITY}",
        message=message,
        app_name="Weather",
        app_icon=None,
        timeout=15,
    )


def main() -> None:
    """
    Запускает программу, выполняет вызовы вышеуказанных функций и обрабатывает вывод.
    """
    weather_data = get_weather(CITY, API_KEY)
    message = format_weather_message(weather_data)
    notify_weather(message)


main()
