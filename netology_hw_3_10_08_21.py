salary=int(input("Введите заработную плату в месяц: "))
mortgage=int(input("Введите какой процент(%) уходит на ипотеку: "))
life=int(input("Введите какой процент(%) уходит на жизнь: "))
mortgage_per_year=mortgage*salary/100*12
life_per_year=life*salary/100*12
saved_per_year=salary*12-mortgage_per_year-life_per_year
print("\n")
print("Вывод:")
print("На ипотеку было потрачено: ", mortgage_per_year)
print("Было накоплено: ", saved_per_year)