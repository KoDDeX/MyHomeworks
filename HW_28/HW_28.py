"""
Домашнее задание № 28

Реализация класса для работы с TXT файлами в стиле ООП
"""
import os


class TxtFileHandler:
    """
    Класс для работы с текстовыми файлами. Этот класс предоставляет методы для чтения, записи и добавления данных в TXT файлы
    """

    def read_file(self, file_path: str, encoding: str = "utf-8-sig") -> str:
        """
        Метод для чтения данных из TXT файла.
        :param file_path: str - Путь к файлу.
        :param encoding: str - Кодировка файла.
        :return: str - Содержимое файла.
        """
        if not os.path.exists(file_path):
            return ""
        with open(file_path, "r", encoding=encoding) as file:
            return file.read()

    def write_file(
        self, file_path: str, data: str, encoding: str = "utf-8-sig"
    ) -> None:
        """
        Метод для записи данных в TXT файл.
        :param file_path: str - Путь к файлу.
        :param data: str - Данные для записи.
        :param encoding: str - Кодировка файла.
        """
        try:
            with open(file_path, "w", encoding=encoding) as file:
                file.write(data)
        except PermissionError as e:
            raise PermissionError(f"Ошибка доступа к файлу файл: {e}")

    def append_file(
        self, file_path: str, data: str, encoding: str = "utf-8-sig"
    ) -> None:
        """
        Метод для дописывания данных в TXT файл.
        :param file_path: str - Путь к файлу.
        :param data: str - Данные для записи.
        :param encoding: str - Кодировка файла.
        """
        with open(file_path, "a", encoding=encoding) as file:
            file.write(data)
