"""
Homework 31

Реализация игры "Города" с использованием паттерна Фасад и датаклассов.
"""
import os
import json
from dataclasses import dataclass, field

DATA_FILE = 'data.json'


@dataclass
class City:
    """
    Датакласс для представления города.
    """
    name: str
    population: str
    subject: str
    district: str
    lat: float
    lon: float
    _is_used: bool = field(default=False)


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
        self.cities = self._create_cities(city_data)
    
    def _create_cities(self, city_data: list[dict]) -> list[City]:
        cities = []
        for city_info in city_data:
            city = City(
                name=city_info['name'],
                population=city_info['population'],
                subject=city_info['subject'],
                district=city_info['district'],
                lat=city_info['coords']['lat'],
                lon=city_info['coords']['lon']
            )
            cities.append(city)
        return cities
    
    def get_all_cities(self) -> set:
        return self.cities


class CityGame:
    """
    Класс, управляющий логикой игры "Города".
    """
    def __init__(self, cities: CitiesSerializer):
        self.cities = cities
        self.used_cities = []
    
    def start_game(self):
        pass

    def human_turn(self, city_input: str):
        pass

    def computer_turn(self):
        pass

    def check_game_over(self):
        pass

    def save_game_state(self):
        pass

class GameManager:
    """
    Фасад, который инкапсулирует взаимодействие между компонентами.
    """
    def __init__(self, json_file: str):
        self.json_file = JsonFile(json_file)
        self.cities = CitiesSerializer(self.json_file.read())
        self.city_game = CityGame(self.cities)


if __name__ == '__main__':
    game_manager = GameManager(DATA_FILE)
    # cities = game_manager.cities_serializer.get_all_cities()
    # print(cities)