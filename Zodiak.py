print("Давайте узнаем ваш знак зодиака!", end="\n\n")
month_of_birth = int(input("Введите месяц рождения (цифрой): "))
day_of_birth = int(input("Введите день: "))
if (month_of_birth == 3 and 21 <= day_of_birth <= 31) or (month_of_birth == 4 and 1 <= day_of_birth <= 20):
    print("\nОвен")
elif (month_of_birth == 4 and 21 <= day_of_birth <= 31) or (month_of_birth == 5 and 1 <= day_of_birth <= 20):
    print("\nТелец")
elif (month_of_birth == 5 and 21 <= day_of_birth <= 31) or (month_of_birth == 6 and 1 <= day_of_birth <= 21):
    print("\nБлизнецы")
elif (month_of_birth == 6 and 22 <= day_of_birth <= 31) or (month_of_birth == 7 and 1 <= day_of_birth <= 22):
    print("\nРак")
elif (month_of_birth == 7 and 23 <= day_of_birth <= 31) or (month_of_birth == 8 and 1 <= day_of_birth <= 22):
    print("\nЛев")
elif (month_of_birth == 8 and 23 <= day_of_birth <= 31) or (month_of_birth == 9 and 1 <= day_of_birth <= 22):
    print("\nДева")
elif (month_of_birth == 9 and 23 <= day_of_birth <= 31) or (month_of_birth == 10 and 1 <= day_of_birth <= 22):
    print("\nВесы")
elif (month_of_birth == 10 and 23 <= day_of_birth <= 31) or (month_of_birth == 11 and 1 <= day_of_birth <= 21):
    print("\nСкорпион")
elif (month_of_birth == 11 and 22 <= day_of_birth <= 31) or (month_of_birth == 12 and 1 <= day_of_birth <= 20):
    print("\nСтрелец")
elif (month_of_birth == 12 and 21 <= day_of_birth <= 31) or (month_of_birth == 1 and 1 <= day_of_birth <= 19):
    print("\nКозерог")
elif (month_of_birth == 1 and 20 <= day_of_birth <= 31) or (month_of_birth == 2 and 1 <= day_of_birth <= 19):
    print("\nВодолей")
elif (month_of_birth == 2 and 20 <= day_of_birth <= 29) or (month_of_birth == 3 and 1 <= day_of_birth <= 20):
    print("\nРыбы")
else:
    print("\nВы ввели неверное значение! Проверьте правильность ввода!")

# решил так, как дошел головой на данном этапе обучения. Уверен, что можно сделать как-то попроще))
# данные по знакам брал отсюда: https://microexcel.ru/znaki-zodiaka/