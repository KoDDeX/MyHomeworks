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
    def read(self):
        """
        Метод чтения данных
        """
        pass

    @abstractmethod
    def write(self, data: list[dict]):
        """
        Метод записи данных
        """
        pass

    @abstractmethod
    def append(self, data: list[dict]):
        """
        Метод добавления данных
        """
        pass

    def __bool__(self):
        """
        Метод проверки существования файла
        """
        if os.path.exists(self.file_path):
            return True
        raise FileNotFoundError(f"Файл '{self.file_path}' не найден.")


class JsonFile(AbstractFile):
    """
    Класс для работы с JSON-файлами.
    """
    def read(self, encoding: str = 'utf-8-sig') -> dict:
        """
        Метод для чтения данных из JSON-файла.
        """
        if self:
            with open(self.file_path, 'r', encoding=encoding) as file:
                return json.load(file)


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
        if self:
            with open(self.file_path, 'r', encoding=encoding) as file:
                json_data = json.load(file)
                json_data.extend(data)
        with open(self.file_path, 'w', encoding=encoding) as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)


class TxtFile(AbstractFile):
    """
    Класс для работы с текстовыми файлами.
    """

    def read(self, encoding: str = 'utf-8-sig') -> list[dict]:
        """
        Метод для чтения данных из текстового файла.
        :encoding: str - кодировка файла.
        """
        if self:
            with open(self.file_path, 'r', encoding=encoding) as file:
                result = list()
                for line in file:
                    row_dict = dict()
                    row = list(map(str, line.strip('\n').split(';')))
                    for i in row:
                        key, value = i.split(':')
                        row_dict[key] = value
                    result.append(row_dict)
                return result

    def write(self, data: list[dict], encoding: str = 'utf-8-sig') -> None:
        """
        Метод для записи данных в текстовый файл.
        :data: list[dict] - данные для записи в файл.
        :encoding: str - кодировка файла.
        """
        with open(self.file_path, 'w', encoding=encoding) as file:
            for row in data:
                result = ""
                for key, value in row.items():
                    result += f"{key}:{value};"
                file.write(result[:-1] + '\n')

    def append(self, data: list[dict], encoding: str = 'utf-8-sig') -> None:
        """
        Метод для добавления данных в существующий текстовый файл.
        :data: list[dict] - данные для добавления в файл.
        :encoding: str - кодировка файла.
        """
        with open(self.file_path, 'a', encoding=encoding) as file:
            for row in data:
                result = ""
                for key, value in row.items():
                    result += f"{key}:{value};"
                file.write(result[:-1] + '\n')


class CsvFile(AbstractFile):
    """
    Класс для работы с CSV-файлами.
    """

    def read(self, delimiter: str = ';', encoding: str = 'utf-8-sig') -> list:
        """
        Метод для чтения данных из CSV-файла.
        """
        if self:
            with open(self.file_path, 'r', encoding=encoding) as file:
                reader = csv.DictReader(file, delimiter=delimiter)
                return list(reader)

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
        with open(self.file_path, 'a', encoding=encoding, newline='') as file:
            for row in data:
                writer = csv.DictWriter(file, fieldnames=row.keys(), delimiter=delimiter)
                writer.writerow(row)
