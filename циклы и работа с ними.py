my_str = 'Hello World'

# print(type(my_str))
# print(my_str.upper())
# print(my_str.lower())
# print(my_str.capitalize())
# print(my_str.title())
# print(my_str.replace('o', '!'))
# help(str.replace)
# my_str.upper()
# print(my_str)

# print(1 + True)

name = 'oleg'
lang = 0.546547

# res = f'Hello, my name is {name.title()}, i know {lang :.1%} a bit'
# print(res)
# my_str = 'Hello World'
# print(my_str[2])
# print(my_str[2:5])
# print(my_str[:5])
# print(my_str[:8:2])
# print(my_str[6:])
# print(my_str[::-1])

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]
income_by_months = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000], ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 15300]]


# print(month_list[2])
# print(month_list[2:5])


# print(income_by_months[2])
# print(income_by_months[2:5])
# income_by_months[0][1] = 13500

# print(income_by_months)

# my_str[0] = '1'
# print(my_str)

# month_list.remove('Jan')
# print(month_list)

# del(month_list[-1])
# print(month_list)

# month_list.append('Oct')
# print(month_list)

# income_by_months.append(['Oct', 15000])
# print(income_by_months)

# print(income_list.count(456456))

# month_list.insert(2, '!!!!!!!!!')
# print(month_list)

# income_by_months.append(['Oct', 15000, ['!!!!!!!']])
# print(income_by_months)

# print(month_list + income_by_months)

# month_list.append(1)
# print(month_list)

# month_list.reverse()
# print(month_list)
# print(month_list[::-1])
# my_str.lower()
# month_list.remove('Jan')
# print(my_str)

# print(month_list)

# res = my_str.lower()
# res_2 = month_list.remove('Jan')
# print(res)

# print(res_2)

# a = [1, 2, 3]
# b = a
# b.append(4)

# print(a)

# a = [1, 2, 3]
# b = a.copy()
# b.append(4)

# print(a)

# month_list.sort()


# res = sorted(month_list)

# print(res)


queries_string = "смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт"

# splitted_str = queries_string.split(',')
# print(sorted(splitted_str))

# print('!!!!!!!!'.join(['Столбец 1', 'Столбец 2', 'Столбец 3']))

salary_tuple = (1000, 1200, 1300, 900, 800)
# print(salary_tuple[0])

# print(sorted(salary_tuple))

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]

# res = zip(month_list, income_list)
# print(dict(res))
# print(len(res))

# tuple_1 = (1, 2)
# tuple_2 = (3, 4)
# res = tuple_1 + tuple_2
# print(res)

# company_tuple = ['Orange', 100000000, 20000]

# name, cap, staff = company_tuple

# print(name)
# print(cap)

# print('Hello' not in 'Hello World')

# company_tuple = ['Apple', 100000000, 20000]
# name = 'Apple'
# if name in company_tuple and 5 > 6:
#   print('Есть!')


# x = 5
# while x != 0:
#     print(x)
#     # x -= 1

# import random

# number = random.randint(0, 100)
# print(number)
# max_tries = 3
# tries = 0

# while tries < max_tries:
#     guess = int(input('Назови свой вариант'))
#     if guess < number:
#         print('Загаданное число больше')
#     elif guess > number:
#         print('Загаданное число меньше')
#     else:
#         print('Ты угадал!')
#         break
#     tries += 1

# if guess != number:
#     print('Вы проиграли')

company_name = 'Orange'

for letter in company_name:
  print(letter)