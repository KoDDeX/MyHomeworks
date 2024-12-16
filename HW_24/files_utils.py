"""
HomeWork 24

Предстоит создать набор функций для работы с файлами различных форматов: JSON, CSV, TXT и YAML. 
Эти функции позволят читать, записывать и обновлять данные в указанных форматах.
Кроме того, создадим тесты для этих функций, чтобы убедиться в корректной работе кода.
"""
import json
import os
import csv
import yaml

def file_exist(file_path: str):
    """
    Функция для проверки существования файла.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл '{file_path}' не существует.")
    return True

def read_json(file_path: str, encoding: str = 'utf-8-sig') -> dict:
    """
    Функция для чтения данных из файла JSON.
    """
    if file_exist(file_path):
        with open(file_path, 'r', encoding=encoding) as file:
            return json.load(file)

def write_json(data: list[dict], file_path: str, encoding: str = "utf-8-sig") -> None:
    """"
    Функция для записи данных в JSON-файл.
    """
    # if file_exist(file_path):
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def append_json(data: list[dict], file_path: str, encoding: str = "utf-8-sig") -> None:
    """
    Функция для добавления данных в существующий JSON-файл
    """
    if file_exist(file_path):
        with open(file_path, 'r', encoding=encoding) as file:
            json_data = json.load(file)
        json_data.extend(data)
        with open(file_path, 'w', encoding=encoding) as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)
        

def read_csv(file_path: str, delimiter: str = ';', encoding: str = 'utf-8-sig') -> list:
    """
    Функция для чтения данных из файла CSV.
    """
    if file_exist(file_path):
        with open(file_path, 'r', encoding=encoding) as file:
            table_list = list(csv.reader(file, delimiter=delimiter))
            return table_list

def write_csv(data: list[dict], file_path: str, delimiter: str = ';', encoding: str = 'utf-8-sig') -> None:
    """
    Функция для записи данных в CSV-файл.
    """
    with open(file_path, 'w', encoding=encoding, newline = "") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(data[0])
        for row in data: 
            writer = csv.DictWriter(file, fieldnames=row.keys(), delimiter=delimiter)
            writer.writerow(row)

def append_csv(data: list[dict], file_path: str, delimiter: str = ';', encoding: str = 'utf-8-sig') -> None:
    """
    Функция для добавления данных в существующий CSV-файл
    """
    if file_exist(file_path):
        with open(file_path, 'a', encoding=encoding, newline= "") as file:
            for row in data:
                writer = csv.DictWriter(file, fieldnames=row.keys(), delimiter=delimiter)
                writer.writerow(row)

def read_txt(file_path: str, encoding: str = 'utf-8-sig') -> str:
    """
    Функция для чтения данных из текстового файла.
    """
    if file_exist(file_path):
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()

def write_txt(data: str, file_path: str, encoding: str = 'utf-8-sig') -> None:
    """
    Функция для записи данных в текстовый файл.
    """
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(data)

def append_txt(data: str, file_path: str, encoding: str = 'utf-8-sig') -> None:
    """
    Функция для добавления данных в существующий текстовый файл
    """
    if file_exist(file_path):
        with open(file_path, 'a', encoding=encoding) as file:
            file.write(data)

def read_yaml(file_path: str, encoding: str = 'utf-8-sig') -> list:
    """
    Функция для чтения данных из файла YAML.
    """
    if file_exist(file_path):
        with open(file_path, 'r', encoding=encoding) as file:
            return yaml.load(file, Loader=yaml.FullLoader)