# "Генераторные сборки"
#

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# генераторная сборка высчитывает разницу длин строк из списков first и second, если их длины не равны. 
# Для перебора строк попарно из двух списков используется функция zip.
first_result = (abs(len(i[0]) - len(i[1])) for i in zip(first, second) if len(i[0]) != len(i[1])) # for j in range(len(second_strings)) if len(i[0]) != len(i[1])) # len(i) for i in first_strings if len(i) >= 5)

# генераторная сборка, содержащая результаты сравнения длин строк в одинаковых позициях из списков first и second. 
# Составлена без использования функции zip. Используются функции range и len.
second_result = [len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i == j]

print(list(first_result))
print(list(second_result))
