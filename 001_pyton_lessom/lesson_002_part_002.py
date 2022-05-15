a = 'Hello'
b = 'World'

print(len('That\'s'))
# перенос строки \n
print('That\ns')
print('hello\nworld')
# тоббуляция \t 4 пробела
print('hello\tn')
# end= в одну строку
print('Hello',end=' ')
print('World')
# cпособ .format заменяет
salary = 1000
salary2 = 2000
name = 'John'
name2 = 'Sarah'
name3 = 'Jack'
emp_string = '{} salary is {}'

print(emp_string.format(name, salary))
print(emp_string.format(name2, salary2))
print(emp_string.format(name3, salary))
# фигурные скобки
device = 'computer'
price = 1090
name = 'Jack'
emp_string2 = 'hello {name:}. Your {device:} costs {price:.2f}'
print(emp_string2.format(name=name, device=device, price=price))
# f в начале строки
name = 'Jack'
salary = 1000
has_licence = True

print(f'Hello {name}. Your salary is {salary - (salary * 0.2):.2f}. it is {has_licence} that you have a licence.')
#decode раскадировать
byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(byte_sting.decode('utf-8'))
print(byte_sting.decode('utf-16'))
print('Hello world'.encode('utf-16'))
# if elif else always start from if
x = 100
if x == 100:
    print(x)

print(x ** 2)
# and or not
x = 100
y = 51
if x == 100 and not y == 50:
    print(x * y)
if 'world' in 'hello world':
        print('hello wold')
# всегда до первого выполненного условия
x = 100
if x > 100:
    print('x > 100')
elif x < 200:
    print('x < 200')
elif x == 200:
        print('x = 150')
#
x = 100
if x > 100:
    print('x > 100')
elif x > 200:
    print('x < 200')
else:
    print('no condition true returned True')
id_code = input('Please enter ID: ')
# if len(id_code) == 12:
#     print(f'Your id is {id_code}')
# elif len(id_code) > 11:
#     print('your id is too long!')
# else:
#     print('your id is too short!')
if len(id_code) == 11:
    print(f"Your id is {id_code} ")
else:
    if len(id_code) < 11:
        print("your code is too short!")
    else:
        print('Your id is too long!')

