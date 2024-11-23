from marvel import small_dict as sd
import os

os.system('cls')
print('----------Задача № 1. Поиск фильмов по названию----------')
user_film = input("Введите фрагмент названия фильма: ")

film_list = list()

# for film in sd.items():
#     if user_film.lower() in film[0].lower():
        # print(film)

for film in sd.keys():
    if user_film.lower() in film.lower():
        film_list.append(film)

print(film_list)
input('Нажмите Enter для продолжения...')

os.system('cls')
print('----------Задача № 2. Фильтрация фильмов по году выхода----------')
user_year = 2024

print('----------Фильмы которые вышли после 2024 года----------')

for film in sd.items():
    if isinstance(film[1], int) and film[1] > user_year:
        print(film)
input('Нажмите Enter для продолжения...')
os.system('cls')

print('----------Просто печатаем названия фильмов----------')
[print(film) for film in sd.keys()]
input('Нажмите Enter для продолжения...')
os.system('cls')

print('----------Собираем список названий фильмов----------')
film_list = list()
film_list = [film for film in sd.keys()]
print(film_list)

input('Нажмите Enter для продолжения...')
os.system('cls')

print('----------Собираем словарь фильтрованный по году----------')
film_dict = dict()
for film in sd.items():
    if isinstance(film[1], int) and film[1] == user_year:
        film_dict[film[0]] = film[1]
print(film_dict)

input('Нажмите Enter для продолжения...')
os.system('cls')

print('----------Собираем список словарей----------')
film_list = [{film: year} for film, year in sd.items()]

print(film_list)