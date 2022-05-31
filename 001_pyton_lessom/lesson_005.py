#def
# print(5 * 10)
# print(10 * 5)
# print(31 * 11)
# def no_parameters():
#     return 'Hello world'
# a = no_parameters()
# print(a)
# print(type(a))
# print(no_parameters())
# sample = []
# print('hello'.upper())
# print(sample.append())
# def squares(number):
#     return number ** 2
#
#
# def print_x():
#     x = 10
#     print(x)
#
#
# x = 5
# print_x()
# print(x)

# def area(a):
#     global x
#     x = 15
#     area = a * x
#     return area
#
#
# def print_area(area):
#     print(f'Area of triangle is {area}')
#
# x = 20
# print_area(area(10))
# print(x)

# def double(number):
#     return number * 2
#
#
# def triple(number):
#     return number * 3
#
#
# def print_double_triple():
#     print(double(triple(10)))
#
#
# print_double_triple()
# def double(number):
#     return number * 2
#
#
# def times_four(number):
#     return double(double(number))

# def print_employee_message(name, age, salary, profession):
#     return f'Hello{name}. You are {age} years old. You work as {profession} with salary of {salary} euro. '
#
#
# workers = [('Jack Smith', 24, 2000, 'programmer'), ('Jack Smith', 24, 2000, 'programmer'), ()]

def print_person_data(a, b, c=1, *arguments, **kwargs):
    print(a, b, c)
    print(arguments)
    for arg in arguments:
        print(arg)
    print(kwargs)
    for arg in kwargs:
        print(arg, kwargs[arg])

print_person_data('Jack', 'Smith', 32, 1231, 'email@gmail.com', y=10, x=20, name='Jack')
