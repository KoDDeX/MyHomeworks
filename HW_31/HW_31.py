"""
Homework 31

Реализация игры "Города" с использованием паттерна Фасад и датаклассов.
"""
import os
import json
from dataclasses import dataclass, field
import random

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
                name=city_info['name'].lower(),
                population=city_info['population'],
                subject=city_info['subject'],
                district=city_info['district'],
                lat=city_info['coords']['lat'],
                lon=city_info['coords']['lon']
            )
            cities.append(city)
        return cities
    
    def get_all_cities(self) -> set:
        return [city.name for city in self.cities]
    
    def get_used_cities(self) -> set:
        return [city.name for city in self.cities if city._is_used]
    
    def use_city(self, city_name: str) -> None:
        for city in self.cities:
            if city.name == city_name:
                city._is_used = True
                break


class CityGame:
    """
    Класс, управляющий логикой игры "Города".
    """
    def __init__(self, cities: CitiesSerializer):
        self.cities = cities
        self.current_city = None
        self.used_cities = []
        self.winner = None
        self.is_human_turn = None
    
    def _dice(self) -> int:
        return random.choice(range(1, 7))

    def _first_move(self) -> bool:
        """
        Метод для определения первого хода игрока.
        """
        while True:
            print('Определим, кто будет ходить первым. Бросаем кубик...')
            input('Нажмите Enter, чтобы бросить кубик...')
            human_dice = self._dice()
            print(f'У вас выпало {human_dice}\nТеперь бросает компьютер...')
            computer_dice = self._dice()
            print(f'У компьютера выпало {computer_dice}')
            if human_dice > computer_dice:
                while not self.current_city:
                    self.human_turn(input('Вы ходите первым. Введите название города: '))
                return True
            elif human_dice == computer_dice:
                print('Ничья!')
            else:
                print('Компьютер ходит первым!')
                return False

    def start_game(self):
        print('Добро пожаловать в игру "Города"!')
        self.is_human_turn = self._first_move()
        while not self.check_game_over():
            if self.is_human_turn:
                self.human_turn(input(f'Введите название города на букву "{self.current_city[-1].upper()}": '))
            else:
                self.computer_turn()
                self.is_human_turn = True
            self.check_game_over()

    def human_turn(self, city_input: str):
        """
        Метод для хода игрока.
        """
        if not city_input:
            print('Вы не ввели город!')
            return
        
        if city_input == 'стоп':
            print('Вы вышли из игры!')
            self.winner = 'Компьютер победил!'
            return
        
        if city_input.lower() not in self.cities.get_all_cities():
                print('Такого города не существует!')
                return
        
        if not self.current_city:
            self.current_city = city_input
            self.cities.use_city(city_input)
            return

        if city_input.lower()[0] != self.current_city[-1]:
            print('Вы неправильно назвали город!')
            return

        if city_input in self.used_cities:
            print('Этот город уже был назван!')
            return

        self.current_city = city_input
        self.cities.use_city(city_input)
        self.is_human_turn = False

    def computer_turn(self):
        pass

    def check_game_over(self) -> bool:
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
    game_manager.city_game.start_game()
    # cities = game_manager.cities_serializer.get_all_cities()
    # print(cities)