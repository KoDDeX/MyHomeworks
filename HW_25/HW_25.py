from pprint import pprint
from marvel import full_dict
from os import system

system("cls")
print(f"1. Импортируем full_dict из файла Marvel.py")
input("Нажмите Enter для продолжения...")
pprint(full_dict)
input("Нажмите Enter для продолжения...")

system("cls")
print(
    f"2. Реализуем ввод от пользователя, который будет принимать цифры через пробел. Разбиваем введённую строку на список и применяем к каждому элементу int, заменяя нечисловые элементы на None с помощью map."
)
user_input: list = list(
    map(
        lambda x: int(x) if "0" <= x <= "9" else None,
        input("Введите цифры через пробел: ").split(),
    )
)
pprint(user_input)
input("Нажмите Enter для продолжения...")

system("cls")
print(
    f"3. Используем filter, чтобы создать словарь, содержащий исходные id и другие ключи, но только для тех фильмов, id которых присутствуют в списке, полученном на предыдущем шаге."
)
input("Нажмите Enter для продолжения...")
films_dict: dict = dict(filter(lambda x: x[0] in user_input, full_dict.items()))
pprint(films_dict)
input("Нажмите Enter для продолжения...")

system("cls")
print(
    f"4. Создаем множество с помощью set comprehension, собрав уникальные значения ключа director из словаря."
)
input("Нажмите Enter для продолжения...")
director_set: set = {val["director"] for val in films_dict.values()}
pprint(f'Режиссёры: {", ".join(director_set)}')
input("Нажмите Enter для продолжения...")

system("cls")
print(
    f"5. С помощью dict comprehension создаем копию исходного словаря full_dict, преобразовав каждое значение year в строку."
)
input("Нажмите Enter для продолжения...")
full_dict_years: dict = {
    k: {k1: str(v1) for (k1, v1) in v.items()} for (k, v) in full_dict.items()
}
pprint(full_dict_years)
input("Нажмите Enter для продолжения...")

system("cls")
print(
    f"6. Используем filter, чтобы получить словарь, содержащий только те фильмы, которые начинаются на букву Ч."
)
input("Нажмите Enter для продолжения...")
full_dict_che: dict = dict(
    filter(
        lambda x: x[1]["title"][0].lower() == "ч" if x[1]["title"] != None else "",
        full_dict.items(),
    )
)
pprint(full_dict_che)
input("Нажмите Enter для продолжения...")

system("cls")
print(
    f"7. Отсортируем словарь full_dict по одному параметру с использованием lambda, создавая аналогичный по структуре словарь. Обязательно укажем, по какому параметру производим сортировку. Параметр title - название фильма."
)
input("Нажмите Enter для продолжения...")
full_dict_sorted: dict = dict(
    sorted(
        full_dict.items(), key=lambda x: x[1]["title"] if x[1]["title"] != None else ""
    )
)
pprint(full_dict_sorted, sort_dicts=False)
input("Нажмите Enter для продолжения...")

system("cls")
print(
    f"8. Отсортируем словарь full_dict по двум параметрам с использованием lambda, создавая аналогичный по структуре словарь. Обязательно укажем, по каким параметрам производим сортировку. Параметры director и title - режиссёр и название фильма."
)
input("Нажмите Enter для продолжения...")
full_dict_sorted_x2: dict = dict(
    sorted(
        full_dict.items(),
        key=lambda x: (
            x[1]["director"],
            x[1]["title"] if x[1]["title"] != None else "",
        ),
    )
)
pprint(full_dict_sorted_x2, sort_dicts=False)
input("Нажмите Enter для продолжения...")

system("cls")
print(
    f"9. **Опционально:** Напишем однострочник, который отфильтрует и отсортирует full_dict с использованием filte` и sorted. Однострочник с использованием фильтрации (по году с 2015) и сортировки по (году и названию)"
)
input("Нажмите Enter для продолжения...")
full_dict_option: dict = dict(
    sorted(
        filter(
            lambda x: x[1]["year"] >= 2015 if isinstance(x[1]["year"], int) else "",
            full_dict.items(),
        ),
        key=lambda x: (
            x[1]["year"] if isinstance(x[1]["year"], int) else "",
            x[1]["title"] if x[1]["title"] != None else "",
        ),
    )
)
pprint(full_dict_option, sort_dicts=False)
input("Нажмите Enter для продолжения...")

"""
10. **Опционально:** Добавим аннотацию типов для переменных, содержащих результаты, и проверим код с помощью mypy. Оставим комментарий о успешной проверке.
mypy HW_25\HW_25.py                                                                     
*** Success: no issues found in 1 source file
"""
