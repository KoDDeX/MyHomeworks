import file_classes
from cities import cities_list

table_list = [
    {"first_name": "Владимир", "middle_name": "Александрович", "last_name": "Монин"},
    {"first_name": "Семен", "middle_name": "Константинович", "last_name": "Беляев"},
    {"first_name": "Дмитрий", "middle_name": "Владимирович", "last_name": "Бобов"},
    {"first_name": "Иван", "middle_name": "Петрович", "last_name": "Бунько"},
    {"first_name": "Никита", "middle_name": "Федорович", "last_name": "Вахрамеев"},
    {"first_name": "Екатерина", "middle_name": "Александровна", "last_name": "Голосняк"},
    {"first_name": "Спартак", "middle_name": "Витальевич", "last_name": "Добровольский"},
    {"first_name": "Григорий", "middle_name": "Сергеевич", "last_name": "Калинин"},
    {"first_name": "Вадим", "middle_name": "Валерьевич", "last_name": "Козлов"},
    {"first_name": "Андрей", "middle_name": "Викторович", "last_name": "Курочкин"},
    {"first_name": "Размик", "middle_name": "Априкович", "last_name": "Мнацаканян"},
    {"first_name": "Алексей", "middle_name": "Николаевич", "last_name": "Охонько"},
    {"first_name": "Даниил", "middle_name": "Дмитриевич", "last_name": "Рукавишников"},
    {"first_name": "Алексей", "middle_name": "Владимирович", "last_name": "Черноусов"},
    {"first_name": "Павел", "middle_name": "Алексеевич", "last_name": "Шарапов"},
    {"first_name": "Кирилл", "middle_name": "Русланович", "last_name": "Шарахудинов"},
    {"first_name": "Дмитрий", "middle_name": "Вячеславович", "last_name": "Юдин"}
]

append_list = [
    {"first_name": "Степан", "middle_name": "Степанович", "last_name": "Степанов"},
    {"first_name": "Иван", "middle_name": "Иванович", "last_name": "Иванов"},
    {"first_name": "Петр", "middle_name": "Петрович", "last_name": "Петров"},
]

# if __name__ == "__main__":
#     # Тестируем JSON
#     json_file = file_classes.JsonFile('./HW_30/test.json')
#     json_file.write(table_list)
#     test_json = json_file.read()
#     print(f'JSON.write.test:\n{test_json}')
#     json_file.append(append_list)
#     test_json = json_file.read()
#     print(f'JSON.append.test:\n{test_json}')

#     # Тестируем CSV
#     csv_file = file_classes.CsvFile('./HW_30/test.csv')
#     csv_file.write(table_list)
#     test_csv = csv_file.read()
#     print(f'CSV.write.test:\n{test_csv}')
#     csv_file.append(append_list)
#     test_csv = csv_file.read()
#     print(f'CSV.append.test:\n{test_csv}')

#     # Тестируем TXT
#     txt_file = file_classes.TxtFile('./HW_30/test.txt')
#     txt_file.write(table_list)
#     test_txt = txt_file.read()
#     print(f'TXT.write.test:\n{test_txt}')
#     txt_file.append(append_list)
#     test_txt = txt_file.read()
#     print(f'TXT.append.test:\n{test_txt}')

if __name__ == "__main__":
    json_file = file_classes.JsonFile('data.json')
    json_file.write(cities_list)