# иттеррация(список. кортеж... можноо разобрать на части. если есть длина и работает len значит объект итеррируемый перебор
courses = ['History', 'Programing', 'Math', 'Literature', 'Physic', 'Math', 'Math']
numbers = [2, 5, 23, 53, 231, 44141, 1412]
# список для каждых элементов
# for subject in courses:
#     print(courses)
#     print(subject)
#     print('Hello world')
# for num in numbers:
#     print(num ** 2)
# sample = 'Hello world'
# for letter in sample:
#     print(letter)
people = [('Roman', 'Smith', 34, 'Male'), ('Mary', 'Gold', 25, 'Female'), ('Jack', 'Jones', 23, None)]

# for person in people:
#     print(f'This is {person[0]} {person[1]}. he is {person[2]} years old. ')

# все значания по очередно присвоится переменным
# for name, surname, age, gender in people:
#     if gender == 'Male':
#         print(f'This is {name} {surname}. he is {age} years old. ')
#     elif gender == 'Female':
#         print(f'This is {name} {surname}. she is {age} years old. ')
#     else:
#         for letter in name:
#             print(letter)
# все комбинации чисел от 1-9
# cnt = 0
# for num1 in range(10):
#     for num2 in range(10):
#         for num3 in range(10):
#             for num4 in range(10):
#                 print(num1, num2, num3, num4)
#                 cnt += 1
# for num in range(1000):
#     if num % 2 == 0:
#         print(num, 'Even')
#     else:
#         print(num, 'Odd')
#
# lst = [1, 2, 3]
# for num in lst:
#     lst.append(num ** 2)
#     print(lst)
result = []
# for num in range(1000):
#     if(num ** 2) % 2 == 0:
#         result.append(num)
# print(result)
id_code = '39801130841'
val = (((int(id_code[0]) * 1) + (int(id_code[1]) * 2) + (int(id_code[2]) * 3) + (int(id_code[3]) * 4) + (int(id_code[4]) * 5) + (int(id_code[5]) * 6) + (int(id_code[6]) * 7) + (int(id_code[7]) * 8) + (int(id_code[8]) * 9) + (int(id_code[9]) * 1)) % 11) < 10
print(val)
val2 = (((int(id_code[0]) * 3 + (int(id_code[1]) * 4) + (int(id_code[2]) * 5) + (int(id_code[3]) * 6) + (int(id_code[4]) * 7) + (int(id_code[5]) * 8) + (int(id_code[6]) * 9) + (int(id_code[7]) * 1) + (int(id_code[8]) * 2) + (int(id_code[9]) * 3))) % 11) < 10
print(val2)
