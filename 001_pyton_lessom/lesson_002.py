string_sample = "Hello world world"
string_sample2 = "first letteR is lowErcase"
string_sample3 = " extra whitespace string "
german_sample = "der Fluß"
#
print(string_sample[0])
print(len(string_sample))
print(string_sample[len(string_sample) - 1])
# последний индекс не включен
print(string_sample[0:5])
# с права на лево
print(string_sample[-1])
print(string_sample[5:-1])
print(string_sample[5:])
print(string_sample[-5:])
# наличие двоеточия указывает на 2 параметра (start:end:step)НА ВЫХОДЕ ТОЖЕ СТРОКА
print(string_sample[::-1])
print(string_sample[0:5] + ' planet ')
#из любой строки можно вырезать любой срез
x = 12324535
# проверка(всегда bool) большие и маленькие буквы имеют разные значения
print('Hello' in string_sample)
# метод uppep
print(string_sample.upper())
print(string_sample)
# метод lower
print(german_sample.lower())
print(german_sample.casefold())
# сделать заглавной первую букву/ capitalaize
print(string_sample2.capitalize())
# делает заглавной каждое слово/ title
print(string_sample2.title())
# обрезает пробелы и символы
print(string_sample.strip(' '))
print(string_sample.lstrip(' '))
print(string_sample.rstrip(' '))
# метод замены и вырезать/чтобы вырезать/string replace
print(string_sample.replace('world', 'planet'))
# count/ считает сколько раз появляется в строке
print(string_sample.count('o'))
# find/ находить индекс только первое слово которое встретилось
print(string_sample.find('world'))
print(string_sample.find('world', 7))
# split создает список
print(string_sample.split())