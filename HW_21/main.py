from cities import cities_list

cities_set = set()
bad_letters = ('ь', 'ъ', 'ы')

cities_set = {city['name'].lower() for city in cities_list}

winner = ''
comp_input = ''
user_input = input('Введите название города или "стоп" для завершения:').lower()
is_user_turn = True

while not winner:
    if is_user_turn:
        if user_input == 'стоп':
            print('Игра завершена. Вы проиграли')
            winner = 'Компьютер победил!'
            break
        elif user_input in cities_set and not comp_input:
            print('Город есть в списке, играем дальше')
            cities_set.remove(user_input)
            is_user_turn = False
        elif user_input in cities_set and comp_input and user_input[0] == comp_input[-1]:
            print('Город есть в списке, играем дальше')
            cities_set.remove(user_input)
            is_user_turn = False
        elif comp_input and user_input[0] != comp_input[-1]:
            print(f'Название города должно начинаться на последнюю букву "{comp_input[-1]}"')
            user_input = input('Введите название города или "стоп" для завершения:').lower()
        else:
            print('Город не найден')
            user_input = input('Введите название города или "стоп" для завершения:').lower()
        if user_input[-1] in bad_letters:
            user_input = user_input[:-1]
    if not is_user_turn:
        for city in cities_set:
            if city[0] == user_input[-1]:
                comp_input = city
                break
        if comp_input:
            print(f'Я выбираю город {comp_input.capitalize()}. Твой ход')
            cities_set.remove(comp_input)
            is_user_turn = True
            user_input = input('Введите название города или "стоп" для завершения:').lower()
        else:
            print('Я проиграл')
            winner = 'Вы победили!'
            break
        if comp_input[-1] in bad_letters:
            comp_input = comp_input[:-1]
print('*********** ', winner, ' ***********')