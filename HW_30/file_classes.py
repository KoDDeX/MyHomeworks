"""
HomeWork 30

Создание классов для работы с различными типами файлов: JSON, TXT и CSV.
"""

import os
import json
import csv

class AbstractFile(ABC):
    def read():
        pass
    def write(data: str):
        pass
    def append(data: str):
        pass


class JsonFile(AbstractFile):
    """
    Класс для работы с JSON-файлами.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self, encoding: str = 'utf-8-sig'):
        """
        Метод для чтения данных из JSON-файла.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding=encoding) as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"Файл '{self.file_path}' не существует.")

    def write(self, data: dict, encoding: str = 'utf-8-sig'):
        """
        Метод для записи данных в JSON-файл.
        """
        with open(self.file_path, 'w', encoding=encoding) as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def append(self, data: dict, encoding: str = 'utf-8-sig'):
        """
        Метод для добавления данных в существующий JSON-файл.
        """
        with open(self.file_path, 'r', encoding=encoding) as file:
            json_data = json.load(file)
        json_data.extend(data)
        with open(self.file_path, 'w', encoding=encoding) as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)


class TxtFile(AbstractFile):
    """
    Класс для работы с текстовыми файлами.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def read(self, encoding: str = 'utf-8-sig'):
        """
        Метод для чтения данных из текстового файла.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding=encoding) as file:
                return file.read()
        else:
            raise FileNotFoundError(f"Файл '{self.file_path}' не существует.")

    def write(self, data: str, encoding: str = 'utf-8-sig'):
        """
        Метод для записи данных в текстовый файл.
        """
        with open(self.file_path, 'w', encoding=encoding) as file:
            file.write(data)

    def append(self, data: str, encoding: str = 'utf-8-sig'):
        """
        Метод для добавления данных в существующий текстовый файл.
        """
        with open(self.file_path, 'a', encoding=encoding) as file:
            file.write(data)


