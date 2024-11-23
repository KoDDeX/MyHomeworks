import os
os.system('cls')

text = input("Введите текст: ")
encrypted_text = ""

try:
    shift = int(input("Введите cдвиг: "))
except:
    print("Ошибка ввода сдвига: не введено число.")
else:
    for char in text:
        if char != " ":
            encrypted_text += chr(ord(char) + shift)
        else:
            encrypted_text += char
    print(f'Результат: {encrypted_text}')
