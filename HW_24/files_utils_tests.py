import files_utils

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

# Тестируем JSON
files_utils.write_json(table_list, './HW_24/test.json')
test_json = files_utils.read_json('./HW_24/test.json')
print(test_json)
files_utils.append_json(append_list, './HW_24/test.json')
test_json = files_utils.read_json('./HW_24/test.json')
print(test_json)

# Тестируем CSV
files_utils.write_csv(table_list, './HW_24/test.csv')
test_csv = files_utils.read_csv('./HW_24/test.csv')
print(test_csv)
files_utils.append_csv(append_list, './HW_24/test.csv')
test_csv = files_utils.read_csv('./HW_24/test.csv')
print(test_csv)       

# Тестируем TXT
files_utils.write_txt(table_list, './HW_24/test.txt')
test_txt = files_utils.read_txt('./HW_24/test.txt')
print(test_txt)
files_utils.append_txt(append_list, './HW_24/test.txt')
test_txt = files_utils.read_txt('./HW_24/test.txt')
print(test_txt)

# Тестируем YAML
test_yaml = files_utils.read_yaml('./HW_24/test.yaml')
print(test_yaml)
