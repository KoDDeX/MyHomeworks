"""
HomeWork 24

Предстоит создать набор функций для работы с файлами различных форматов: JSON, CSV, TXT и YAML. 
Эти функции позволят читать, записывать и обновлять данные в указанных форматах.
Кроме того, создадим тесты для этих функций, чтобы убедиться в корректной работе кода.
"""
import json

def file_exist(file_path: str) -> bool:
    """
    Функция для проверки существования файла.
    """
    return os.path.exists(file_path)

def read_json(file_path: str, encoding: str = 'utf-8') -> dict:
    """
    Функция для чтения данных из файла JSON.
    """
    if not file_exist(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")
    else:
        with open(file_path, 'r', encoding=encoding) as file:
            return json.load(file)

