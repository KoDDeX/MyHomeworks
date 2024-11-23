student_name = input("\nВведите имя студента: ")
student_rank = input("Введите оценку студента: ")

if student_rank.isdigit() and 1 <= int(student_rank) <= 3:
    print(f"\nИмя студента:\t{student_name}.\nУровень:\tНачальный.")
elif student_rank.isdigit() and 4 <= int(student_rank) <= 6:
    print(f"\nИмя студента:\t{student_name}.\nУровень:\tСредний.")
elif student_rank.isdigit() and 7 <= int(student_rank) <= 9:
    print(f"\nИмя студента:\t{student_name}.\nУровень:\tДостаточный.")
elif student_rank.isdigit() and 10 <= int(student_rank) <= 12:
    print(f"\nИмя студента:\t{student_name}.\nУровень:\tВысокий.")
else:
    print("Ошибка: Введена некорректная оценка.") # В таком формате условных операторов более правильно обрабатываются ошибки: в случае если введено не число, а также оценка за рамками 1-12.