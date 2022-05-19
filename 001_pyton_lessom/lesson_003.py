empty_list = []
# любой тип данных модет быть элементом списка
# world = 'world'
# filled_list = [123, 0.123, 'hello', world, True, None, [1, ['h', 'e', 'l', 'l','o'], 3, 4, 5]]
# print(filled_list)
# print(filled_list[1], filled_list[3], filled_list[5])
# print(filled_list)
# print(filled_list[6][1])
# print(filled_list[6][1][2])
#
# print(filled_list[2][1:3])

# courses = ['History', 'Programming', 'Math', 'Literature', 'Physic']
# nums = [1, 5, 6, 8, 3, 4, 2]
#
# courses.append([1, 2, 3, 4, 5])
# print(courses[3:])
# insert element вставлять в любую часть списка
# courses.insert(1, 'Biology')
# print(courses)
# print(len(courses))
# courses = ['History', 'Programming', 'Math', 'Literature', 'Physic']
# nums = [1, 5, 6, 8, 3, 4, 2]
# extend разбирает на части
# new_courses = ['Economics', 'Marketing', [1, 2, 3, 4]]
# courses.extend(new_courses)
# print(courses)
# newcourses = 'hello'
# print(list(newcourses))
# courses.extend(newcourses)
# remove удаление
# courses.remove('Math')
# print(courses)
# pop удаляет последний элемент
# a = courses.pop()
# print(courses)
# print(a)
# сортируется по порядку unicode
# courses = ('History', 'Programming', 'Math', 'Literature', 'Physic')
# nums = [1, 5, 6, 8, 3, 4, 2]
# print(courses[::-1])
# courses.reverse()
# courses.sort()
# развернуть список
# courses.sort(reverse=True)
# print(courses)
#
# nums.sort()
# print(nums)
# print(sorted(courses))
# print(courses)
# минимальное значение
# print(min(courses))
# print(max(courses))
# сумма только числа
# print(sum(nums))
# метод find index возвращает номер индекса
# print(courses.index('Math'))
# print(courses[courses.index('Math')])
# проверка на наличие
# print('Math' in courses)
# списки и срезы модно складывать
# print(courses[:2] + nums[:3])
# print((courses[1:3]) + (courses[:1]))
# courses_str = ','.join(courses)
# print(courses_str)
# разделять и вставлять символы
# print(courses[0] + '   ' + courses[1])
# user_input = input('Enter something: ')
# new_list = user_input.split(', ')
# print(new_list)
# a, b, c, = input('Enter something: ').split()
# print(a)
# print(b)
# print(c)
# a = 10
# b = a
# b = 2
# print(b)
# print(a)

# courses2 = courses.copy()
# courses2[0] = 'Art'
# courses[-1] = 'Biology'

# print(courses)
# print(courses2)
#
# sample = [1, 2, 3]
# if sample:
#     print('OK')
# else:
#     print('NON')
# tuple чтобы объявить кортеж из одного элемента нудно добавть ,

empty_tuple = 1, 2, 3
# print(type(empty_tuple))
# print(courses.index('Math'))
# print(nums.count(1))
#
# courses = list(courses)
# courses.insert(1, 'Art')
# courses = tuple(courses)
# print(courses)
# print(id(courses))
# set множество
courses = {'History', 'Programming', 'Math', 'Literature', 'Math', 'Physic'}
nums = {1, 5, 6, 8, 3, 4, 2, 2, 4, 4, 1, 1,}

empty_set = ()
# избавляется от дубликатов, нет порядка
print(type(empty_set))
print(list(set(nums)))
print(courses)
# числа выходят по порядку обратиться не можем не индексируемый элемент
print(nums)
# add
courses.add('Art')
print(courses)
# remove уда
courses.remove('Math')
print(courses)
# pop
a = courses.pop()
print(courses)
print(a)
# discard same as remove
a = courses.discard('Math')
print(courses)
# update same as extend in list
courses.update(nums)
print(courses)
# intersection
set1 = {'Math', 'History', 'Programing', 'Physics'}
set2 = {'History', 'Physics'}

print(set2.intersection(set1))
# difference
print(set1.difference(set2))
print(set2.difference(set1))
#сет2 является подмножеством сет 1 абсолютное дублирование значений
print(set1.issubset(set2))
print(set2.issubset(set1))
# включает ли оно в себя подмножество сет 2
print(set1.issuperset(set2))
print(set2.issuperset(set1))
#
courses = list(set(courses))
print(courses)
