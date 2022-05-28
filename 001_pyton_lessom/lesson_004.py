# sample1 = 'Hello world'
# sample2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for letter in sample2:
#     print(letter)

# people = [('Jack', 'Smith', 35, 'male'), ('Mary', 'Gold', 25, 'female'), ('Bob', 'Summer', 15, 'male'),('Bob', 'Summer', 15, None)]
#
# for name, surname, age, gender in people:
#     if gender == 'male':
#         if age < 12:
#             print(f'This is {name} {surname}. He is child.')
#         elif age < 18:
#             print(f'This is {name} {surname}. He is teenager.')
#         else:
#             print(f'This is {name} {surname}. He is adult')
#     elif gender == 'female':
#         if age < 12:
#             print(f'This is {name} {surname}. She is child.')
#         elif age < 18:
#              print(f'This is {name} {surname}. She is teenager.')
#         else:
#             print(f'This is {name} {surname}. She is adult')
#     else:
#         print('Sorry we can\'t print your massage')
# primes = []
#
# for number in range(1, 101):
#     cnt = 0
#     for num in range(1, 101):
#         if number % num == 0:
#             cnt += 1
#     if cnt == 2:
#         primes.append(number)
# print(primes)
# cnt = 0
# while cnt < 100:
#     print(f'I can\'t stop{cnt}')
#     cnt += 1
# distance_to_target = float(input('How many kilometers you need to make? '))
# current_position = 0
#
# step = 0.4
# step_cnt = 0
# while current_position < distance_to_target * 1000:
#     if step_cnt % 1000 == 0:
#         print(step_cnt)
#     current_position += step
#     step_cnt += 1
# цикл for while
# while True:
#     user_input = input('Please enter ID code: ')
#     if user_input.lower() == 'exit':
#         print('Good Bye')
#         break
#     else:
#         if len(user_input) != 11:
#             if len(user_input) > 12:
#                 print('Too long')
#             else:
#                 print('Too short')
#         else:
#             print(user_input)
#             break
#  pass
# x = 5
# if x == 5:
#     pass
# elif x > 5:
#     pass
# elif x < 5:
#     pass
#     print('Hello')
# for letter in 'Python':
#     if letter == 'o':
#         break
#     elif letter == 't':
#         continue
#     print(letter)
#
# print('Good Bye!')
# user_input = input('Plese enter ID: ')
# if user_input.isdigit():
#     print(user_input)
# else:
#     print('Fail')
#try except обязательно else может не быть finally выполняется всегда
# user_input = input('Please enter ID code: ')
# int(user_input)
while True:
    try:
        user_input = input('Please enter ID code: ')
        int(user_input)
        if len(user_input) != 11:
            raise UserWarning

    except ValueError:
        print('Code you\'ve entered is not numeric')
        continue
    except UserWarning:
        if len(user_input) > 11:
            print('Too long')
        else:
            print('Too short')
        continue

    else:
        print(f'Your id is {user_input}')
        break
print('Good bye')