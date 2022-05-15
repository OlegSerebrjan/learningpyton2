# Integer (int)
# Float (float)
# String (str)
# Boolean (bool)
# None type
a = 16354
b = 320
print(100 + b)
# drobe number
print(a / b)
# whole number
print(a // b)
# make it too full numbers
print(round(1.5 * 10))
print(round(2.5 * 10))
print(round(3.5 * 10))
#остаток при делении
print(a % b)
# возведение в стапень
print(a ** b)
# порядок множителей
print (a + b ** 2)
#  сложение строк, только слодение и умножение. число привести к типу данных строка
a = 'hello'
b = 'my name is '
c = 'Oleg'
d = 'my age is'
e = 24.
print(a +' ' + b + c + ' ' + d + ' ' + str(e))
print(type(e))
# конвертация е в строку
e = str(e)
print(type(e))
# конвертация int to float на выхоле всегда float
e = 24.18746
print(float(e))
print(10 * 0.251 ** 3 % 0.2)
print(int(e))
e = '24.136315'
print(float(e))
# конвертиция в int
print(int(float(e)))
# конвертиация в bool True = 1; False = 0
print(int(True))
print(int(False))
print(True + 2)
print(float(True))
print(float(False))
#
a = '1'
print(bool(a))
a = ''
print(bool(a))
# конвертиция None to bool
a = None
print(bool(a))
# конвертиция в None нет
# пример
a = 231
b = 0.5725
d = 'oleg'
e = None
print(str(a) + str(b)+' ' + d + ' ' + str(e))
x = '222'
print(int(x) + 2)
# input всегда на выходе получается строка
# user_input = input('your name')
# print(typr(user_input))
# # калькулятор сторон треугольника
# side_a = input('please enter side A:')
# side_b = input('please enter side B:')
# side_c = input('please enter side C:')
# вычесление не используются как строка
side_a = float(input('please enter side A:'))
side_b = float(input('please enter side B:'))
side_c = float(input('please enter side C:'))

half_perimeter = (side_a + side_b + side_c) / 2

area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) ** 0.5
print(area)

