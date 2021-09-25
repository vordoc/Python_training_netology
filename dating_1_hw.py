boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
s_boys = sorted(boys)
s_girls = sorted(girls)
couples = list(zip(s_boys, s_girls))


if len(s_boys)==len(s_girls):
    print("Идеальные пары:")
    for best_couples in couples:
        print(f"{best_couples[0]} и {best_couples[1]}")
else:
    print("Внимание! Кто-то может остаться без пары!")

# проверяем, добавим в список мужчин еще одно имя

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Viktor']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
s_boys = sorted(boys)
s_girls = sorted(girls)
couples = list(zip(s_boys, s_girls))


if len(s_boys)==len(s_girls):
    print("Идеальные пары:")
    for best_couples in couples:
        print(f"{best_couples[0]} и {best_couples[1]}")
else:
    print("Внимание! Кто-то может остаться без пары!")

# добавим еще пару имен в список женщин

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha', 'Maria', 'Alexa']
s_boys = sorted(boys)
s_girls = sorted(girls)
couples = list(zip(s_boys, s_girls))


if len(s_boys)==len(s_girls):
    print("Идеальные пары:")
    for best_couples in couples:
        print(f"{best_couples[0]} и {best_couples[1]}")
else:
    print("Внимание! Кто-то может остаться без пары!")

# Done