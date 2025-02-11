"""
Homework 31

Реализация игры "Города" с использованием паттерна Фасад и датаклассов.
"""
import os
import json
from dataclasses import dataclass, field
import random

DATA_FILE = 'data.json'
GAME_STATE = 'game_state.json'
BAD_LETTERS = ('ь', 'ъ', 'ы')

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
            if city_info.get('cities'):
                cities.append(
                    {'game_state_info':{
                        'current_city': city_info['current_city'],
                        'is_human_turn': city_info['is_human_turn'],
                        'human_first_turn': city_info['human_first_turn']
                    }
                }
                )
            else:
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
    
    def get_unused_cities(self, first_char: str) -> set:
        return [city.name for city in self.cities if not city._is_used and city.name[0] == first_char]
    
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
        self.game_state_data = {}
        if isinstance(cities.cities[0],dict):
            self.game_state_data = cities.pop(0)
        self.cities = cities
        self.current_city = self.game_state_data.get('current_city', None)
        self.winner = None
        self.is_human_turn = self.game_state_data.get('is_human_turn', None)
        self.human_first_turn = self.game_state_data.get('human_first_turn', None) # True -- человек ходит первым, False - компьютер ходит первым. Для подведения итогов
    
    def _dice(self) -> int:
        return random.choice(range(1, 7))

    def _first_move(self) -> bool:
        """
        Метод для определения первого хода игрока.
        """
        while True:
            print('Определим, кто будет ходить первым.')
            self.human_turn(input('Нажмите Enter, чтобы бросить кубик...'), True)
            if self.winner:
                break
            human_dice = self._dice()
            print(f'У вас выпало {human_dice}\nТеперь бросает компьютер...')
            computer_dice = self._dice()
            print(f'У компьютера выпало {computer_dice}')
            if human_dice > computer_dice:
                while not self.current_city:
                    self.human_turn(input('Вы ходите первым. Введите название города: ').lower())
                    self.human_first_turn = True
                return False
            elif human_dice == computer_dice:
                print('Ничья!')
            else:
                print('Компьютер ходит первым!')
                self.computer_turn()
                self.human_first_turn = False
                return True

    def set_current_city(self, city_name: str) -> None:
        """
        Метод для использования города.
        """
        self.cities.use_city(city_name)
        self.current_city = city_name
        if self.current_city[-1] in BAD_LETTERS:
            self.current_city = self.current_city[:-1]

    def start_game(self):
        print('Добро пожаловать в игру "Города"!\nВ любой момент вы можете ввести "стоп", чтобы выйти из игры.\n')
        self.is_human_turn = self._first_move()
        while not self.check_game_over():
            if self.is_human_turn:
                self.human_turn(input(f'Введите название города на букву "{self.current_city[-1].upper()}": ').lower())
            else:
                self.computer_turn()

    def human_turn(self, city_input: str, first_move: bool = False) -> None:
        """
        Метод для хода игрока.
        """
        if city_input.lower() == 'стоп':
            if input('Хотите сохранить игру? (y/n): ').lower() == 'y':
                self.save_game_state()
            print('Вы вышли из игры!')
            self.winner = 'Компьютер победил!'
            return

        if first_move:
            return

        if not city_input:
            print('Вы не ввели город!')
            return
        
        if city_input.lower() not in self.cities.get_all_cities():
                print('Такого города не существует!')
                return
        
        if not self.current_city:
            self.set_current_city(city_input)
            self.is_human_turn = False
            return

        if city_input.lower()[0] != self.current_city[-1]:
            print('Вы неправильно назвали город!')
            return

        if city_input in self.cities.get_used_cities():
            print('Этот город уже был назван!')
            return

        self.set_current_city(city_input)
        self.is_human_turn = False

    def computer_turn(self):
        """
        Метод для хода компьютера.
        """
        if not self.current_city:
            comp_city = random.choice(self.cities.get_all_cities())
        else:
            comp_city = random.choice(self.cities.get_unused_cities(self.current_city[-1]))
        print(f'Компьютер назвал город {comp_city.title()}')
        self.set_current_city(comp_city)
        self.is_human_turn = True
        return
        

    def check_game_over(self) -> bool:
        if self.winner:
            print(self.winner)
            return True
        if not self.cities.get_unused_cities(self.current_city[-1]):
            if self.is_human_turn and self.human_first_turn:
                print('Ничья!\nСписок городов закончился!')
            elif self.is_human_turn and not self.human_first_turn:
                print('Компьютер победил!')
            else:
                print('Вы победили!')
            return True
        return False

    def save_game_state(self):
        """
        Метод для сохранения состояния игры и выхода.
        """
        self.game_state_data = [{
            'current_city': self.current_city,
            'is_human_turn': self.is_human_turn,
            'human_first_turn': self.human_first_turn
        }]
        for city in self.cities.cities:
            self.game_state_data.append(
                {
                    'name': city.name,
                    'population': city.population,
                    'subject': city.subject,
                    'district': city.district,
                    'coords': {
                        'lat': city.lat,
                        'lon': city.lon
                    }
                }
            )
        self.json_file = JsonFile(GAME_STATE)
        self.json_file.write(self.game_state_data)
        exit()

class GameManager:
    """
    Фасад, который инкапсулирует взаимодействие между компонентами.
    """
    def __init__(self, json_file: str, game_state_file: str = GAME_STATE):
        if os.path.exists(game_state_file) and input('Хотите продолжить игру? (y/n): ').lower() == 'y':
            self.json_file = JsonFile(game_state_file)
        else:
            self.json_file = JsonFile(json_file)
        self.cities = CitiesSerializer(self.json_file.read())
        self.city_game = CityGame(self.cities)


if __name__ == '__main__':
    game_manager = GameManager(DATA_FILE)
    game_manager.city_game.start_game()
    # cities = game_manager.cities_serializer.get_all_cities()
    # print(cities)