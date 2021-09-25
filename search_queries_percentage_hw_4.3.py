queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


storage = {}

for query in queries:
    words_count = query.split()
    if len(words_count) in storage.keys():
        storage[len(words_count)] += 1
    else:
        storage.update({len(words_count): 1})
# print(storage)

for k, v in storage.items():
    q_percent = round((v / len(queries)) * 100)
    print(f'Поисковых запросов из {k} слов: {q_percent}%')






