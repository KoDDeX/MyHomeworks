from marvel import full_dict

user_input = list(map(lambda x: int(x) if "0" <= x <= "9" else None, input("Введите цифры через пробел: ").split()))

# lst = list(filter(lambda x, y: y['title'] if x in user_input else None, full_dict.keys()))
lst = dict(filter(lambda x: x[0] in user_input, full_dict.items()))

