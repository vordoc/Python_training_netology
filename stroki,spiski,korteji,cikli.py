name = "igor"
cash = 0.545458

res = f"Hello, my name is {name.title()}, i have {cash: .1%}"
print(res)
print(res[0])
print(res[0:5])
print(res[0:10:2])
print(res[::2])

list_1 = [["jun", 256], ["jul", 523], ["aug", 482]]
print(list_1[1][1])
list_2 = list_1.copy()
list_2.append(["sep", 255]) # добавиляем список в список:)
print(list_2)

str_1 = "Dana, Oleg Evgenievich, Nikolay, Petr"
list_3 = str_1.split(",")
print(list_3)