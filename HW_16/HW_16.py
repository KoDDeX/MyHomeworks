import math

# Выводим приветствие первого задания
print('\n\nЗадание №1: Конвертация секунд') 
seconds_count = int(input('Введите количество секунд: ')) # Сделаем приведение к int, т.к. входное значение может быть не целочисленным

hours = seconds_count // 3600 # Получаем целочисленное деление на 3600, т.к. в 1 часе 3600 секунд
minutes = (seconds_count % 3600) // 60 # Получаем остаток от деления на 3600 и делим на 60, т.к. в 1 минуте 60 секунд
seconds = seconds_count % 60 # Получаем остаток от деления на 60

print(f'В указанном количестве секунд {seconds_count}:\nЧасов: {hours}\nМинут: {minutes}\nСекунд: {seconds}\n') # Выводим результаты в заданном формате

# Делаем паузу для того, чтобы пользователь успел прочитать результаты
input('Нажмите Enter для продолжения...')

# Выводим приветствие второго задания
print('\n\nЗадание №2: Конвертация температуры') 
# # Вариант № 1
# temperature_celsius = round(float(input('Введите температуру в градусах Цельсия: ')),2) # Сделаем округление до сотых, на всякий случай, при помощи обычного round
# Calvin = temperature_celsius + 273.15 # Можно не округлять, т.к. входное значение уже округлено
# Fahrenheit = temperature_celsius * 1.8 + 32
# Reomur = temperature_celsius * 0.8
# # Выводим результаты в заданном формате. Не получится вывести в заданном формате используя отладочные строки. Но округлим по-модному (для python 3.6 и выше)
# print(f'Если температура в градусах Цельсия равна {temperature_celsius:.2f}°C, то:\nКельвин: {temperature_celsius:.2f}°C + 273.15 = {Calvin:.2f}°K\nФаренгейт: ({temperature_celsius:.2f}°C × 9/5) + 32 = {Fahrenheit:.2f}°F\nРеомюр: {temperature_celsius:.2f}°C × 4/5 = {Reomur:.2f}°Ré\n') # if не проходили, ато бы проверил дробное число или целое, чтобы вывести красивее. А почему бы и нет....

# # Вариант № 2
# temperature_celsius = float(input('Введите температуру в градусах Цельсия: '))
# if temperature_celsius % 1 == 0:
#     temperature_celsius = int(temperature_celsius)
# else:
#     temperature_celsius = round(temperature_celsius,2)

# Calvin = temperature_celsius + 273.15
# if Calvin % 1 == 0:
#     Calvin = int(Calvin)
# else :
#     Calvin = round(Calvin,2)

# Fahrenheit = temperature_celsius * 1.8 + 32
# if Fahrenheit % 1 == 0:
#     Fahrenheit = int(Fahrenheit)
# else :
#     Fahrenheit = round(Fahrenheit,2)

# Reomur = temperature_celsius * 0.8
# if Reomur % 1 == 0:
#     Reomur = int(Reomur)
# else :
#     Reomur = round(Reomur,2)
    
# print(f'Если температура в градусах Цельсия равна {temperature_celsius}°C, то:\nКельвин: {temperature_celsius}°C + 273.15 = {Calvin}°K\nФаренгейт: ({temperature_celsius}°C × 9/5) + 32 = {Fahrenheit}°F\nРеомюр: {temperature_celsius}°C × 4/5 = {Reomur}°Ré\n') # А если бы мы еще проходили функции, то можно было бы сделать красиво. Но пока не проходили. Хотя.......

# Вариант № 3
def convert_temperature(temperature): # Делаем функцию, которая будет принимать температуру и возвращать целое число или float если дробь
    if temperature % 1 == 0:
        return int(temperature)
    else:
        return round(temperature,2)

temperature_celsius = float(input('Введите температуру в градусах Цельсия: '))
Calvin = temperature_celsius + 273.15
Fahrenheit = temperature_celsius * 1.8 + 32
Reomur = temperature_celsius * 0.8

# Выводим результат в заданной форме, конвертируя в int или float если дробное число
print(f'Если температура в градусах Цельсия равна {convert_temperature(temperature_celsius)}°C, то:\nКельвин: {convert_temperature(temperature_celsius)}°C + 273.15 = {convert_temperature(Calvin)}°K\nФаренгейт: ({convert_temperature(temperature_celsius)}°C × 9/5) + 32 = {convert_temperature(Fahrenheit)}°F\nРеомюр: {convert_temperature(temperature_celsius)}°C × 4/5 = {convert_temperature(Reomur)}°Ré\n') 

input('Нажмите Enter для выхода...')
