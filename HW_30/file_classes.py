"""
HomeWork 30

Создание классов для работы с различными типами файлов: JSON, TXT и CSV.
"""
from abc import ABC, abstractmethod
import os
import json
import csv

class AbstractFile(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def read():
        pass

    @abstractmethod
    def write(data: str):
        pass

    @abstractmethod
    def append(data: str):
        pass


class JsonFile(AbstractFile):
    """
    Класс для работы с JSON-файлами.
    """
    def read(self, encoding: str = 'utf-8-sig') -> dict:
        """
        Метод для чтения данных из JSON-файла.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding=encoding) as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"Файл '{self.file_path}' не найден.")

    def write(self, data: list[dict], encoding: str = 'utf-8-sig') -> None:
        """
        Метод для записи данных в JSON-файл.
        """
        with open(self.file_path, 'w', encoding=encoding) as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def append(self, data: list[dict], encoding: str = 'utf-8-sig') -> None:
        """
        Метод для добавления данных в существующий JSON-файл.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding=encoding) as file:
                json_data = json.load(file)
        json_data.extend(data)
        with open(self.file_path, 'w', encoding=encoding) as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)


class TxtFile(AbstractFile):
    """
    Класс для работы с текстовыми файлами.
    """

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


class CsvFile(AbstractFile):
    """
    Класс для работы с CSV-файлами.
    """

    def read(self, delimiter: str = ';', encoding: str = 'utf-8-sig') -> list:
        """
        Метод для чтения данных из CSV-файла.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding=encoding) as file:
                table_list = list(csv.reader(file, delimiter=delimiter))
                return table_list
        else:
            raise FileNotFoundError(f"Файл '{self.file_path}' не существует.")

    def write(self, data: list[dict], delimiter: str = ';', encoding: str = 'utf-8-sig') -> None:
        """
        Метод для записи данных в CSV-файл.
        """
        with open(self.file_path, 'w', encoding=encoding, newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerow(data[0])
            for row in data: 
                writer = csv.DictWriter(file, fieldnames=row.keys(), delimiter=delimiter)
                writer.writerow(row)

    def append(self, data: list[dict], delimiter: str = ';', encoding: str = 'utf-8-sig') -> None:
        """
        Метод для добавления данных в существующий CSV-файл.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'a', encoding=encoding, newline='') as file:
                for row in data:
                    writer = csv.DictWriter(file, fieldnames=row.keys(), delimiter=delimiter)
                    writer.writerow(row)
