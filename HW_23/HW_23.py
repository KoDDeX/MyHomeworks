"""
Домашнее задание №23

Создание погодного приложения на Python.
"""

import requests
from plyer import notification

API_KEY = r'167349a6d42610462c6f5bd91a7c2e36'

def get_weather(city: str, api_key: str) -> dict:
    """
    Выполняет запрос к API и возвращает данные о погоде в виде словаря.
    """ 
    url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    return response.json()

def format_weather_message(weather_dict: dict) -> str:
    """
    Форматирует данные о погоде в удобочитаемое сообщение.
    """
    return f'Температура воздуха: {weather_dict["main"]["temp"]}°C\nОщущается как: {weather_dict["main"]["feels_like"]}°C\nописание: {weather_dict["weather"][0]["description"]}'

def notify_weather (message: str) -> None:
    """
    Отправляет уведомление пользователю с информацией о погоде.
    """
    notification.notify(
        title='Погода',
        message=message,
        timeout=10
    )
