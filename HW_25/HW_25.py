from marvel import full_dict
from pprint import pprint

user_input = list(map(lambda x: int(x) if "0" <= x <= "9" else None, input("Введите цифры через пробел: ").split()))
# pprint(user_input)

films_dict = dict(filter(lambda x: x[0] in user_input, full_dict.items()))
# pprint(films_dict)

director_set = {val['director'] for val in films_dict.values()}
# pprint(f'Режиссёры: {", ".join(director_set)}')

full_dict_years = {k:{k1:str(v1) for (k1, v1) in v.items()} for (k, v) in full_dict.items()}
# pprint(full_dict_years)

full_dict_che = dict(filter(lambda x: x[1]['title'][0].lower() == 'ч', full_dict_years.items()))
# pprint(full_dict_che)

# Отсортировал словарь по названию фильма ['title']
full_dict_sorted = dict(sorted(full_dict.items(), key=lambda x: x[1]['title'] if x[1]['title'] != None else ''))
# pprint(full_dict_sorted, sort_dicts=False)

# Осортировал словарь по режисеру ['director'] и названию фильма ['title']
full_dict_sorted_year = dict(sorted(full_dict.items(), key=lambda x: (x[1]['director'], x[1]['title'] if x[1]['title'] != None else '')))
# pprint(full_dict_sorted_year, sort_dicts=False)