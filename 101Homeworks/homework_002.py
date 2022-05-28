example_string = "Hello bro"
print((example_string[0:2]) + (example_string[7:9]))

example_string2 = 'jack Is My NAME'
print(example_string2.capitalize())

example_string3 = 'Get rid of stars please*'
print(example_string3.strip('*'))

example_string4 = 'hello my name is jack'
print(example_string4.capitalize())
print(example_string4.upper()[-4])

var1 = 'jack'
var2 = 'hello'
var3 = 'my name is'
emp_string = f'{var2} {var3} {var1}'
print(emp_string.format(var1=var2, var2=var3, var3=var1))

byte_string = b"\316\273"
print(byte_string.decode('utf-16'))

example_string5 = "It cost me 1000.00$"
cost = 1000
if cost > 500:
    print(True)
else:
    print(False)







