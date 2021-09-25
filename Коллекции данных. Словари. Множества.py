capitals_dict = {'Russia': 'Moscow', 'Ukraine': 'Kiev'}
print(capitals_dict['Russia']) # по ключу russia вызываем значение moscow
print()

for country, capital in capitals_dict.items(): # items возвращает и ключ и значение
    print(country, '->', capital)
print()

capitals_dict['France'] = 'Paris' # добавляем в словарь новый ключ и значение
print(capitals_dict)
print()

for country in capitals_dict.keys(): # перебор ключей
    print(country)
print()

for capital_1 in capitals_dict.values(): # перебор значений
    print(capital_1)