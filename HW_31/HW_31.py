"""
Homework 31

Реализация игры "Города" с использованием паттерна Фасад и датаклассов.
"""
import os
import json

class JsonFile:
    """
    Класс отвечающий за чтение и запись данных в формате JSON.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self, encoding: str = 'utf-8-sig') -> list[dict]:
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

    def __bool__(self):
        """
        Метод проверки существования файла
        """
        if os.path.exists(self.file_path):
            return True
        raise FileNotFoundError(f"Файл '{self.file_path}' не найден.")


class CitiesSerializer:
    """
    Класс, использующий датакласс City для хранения информации о городах.
    """
    def __init__(self, city_data: list[dict]):
        self.city_data = {City(
            city_data['name'],
            city_data['population'],
            city_data['subject'],
            city_data['district'],
            city_data['coords']['lat'],
            city_data['coords']['lon']
        )}
    
    def get_all_cities(self) -> set:
        return self.city_data


class City:
    """
    Датакласс для представления города.
    """
    def __init__(self, name: str, population: int, subject: str, district: str, latitude: str, longitude: str):
        self.name = name
        self.population = population
        self.subject = subject
        self.district = district
        self.latitude = latitude
        self.longitude = longitude
        self._is_used = False


class GameManager:
    """
    Фасад, который инкапсулирует взаимодействие между компонентами.
    """
    def __init__(self, json_file: str):
        self.json_file = JsonFile(json_file)
        self.cities_serializer = CitiesSerializer(self.json_file.read())