# len показывает количество символов в строке - длину строки
# print(len("abc"))

# x=7
# if x % 2 == 0:
#     print(x, "четное число")
# else:
#     print(x, "нечетное число")

height = int(input("Введите рост: "))
age = int(input("Введите возраст: "))
kids_count = int(input("Количество детей: "))
student = int(input("Учится ли человек сейчас? да - введите 1, нет - введите 0: "))
if 18 <= age <= 27 and kids_count < 2 and student == 0:
 if height < 170:
    print("В танкисты")
 elif height < 185:
    print("На флот")
 elif height < 200:
    print("В десантники")
 else:
    print("В другие войска")
else:
    print("Не призывается")
