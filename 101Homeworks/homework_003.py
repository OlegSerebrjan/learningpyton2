# 0-100
# Если число делится на 3 без остатка - написать число и Fizz
# Если число делится на 5 без остатка - написать число и Buzz
# Если число делится на 3 и на 5 без остатка - написать число и FizzBuzz
for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        print(str(num) + ('FizzBuzz'))
    elif num % 3 == 0:
        print(str(num) + ('Fizz'))
    elif num % 5 == 0:
        print(str(num) + ('Buzz'))

