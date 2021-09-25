geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
# result = [geo_log for geo_log in geo_logs if "Россия" in next(iter(geo_log.values()))]
# print(result)


# list_russia = []
# for i in geo_logs:
#     if 'Россия' in next(iter(i.values())):
#         print(list(i)

vr = []
for visits in geo_logs:
  for visit,[City,Country] in visits.items():
    if Country == 'Россия':
        vr.append(visits)
print(vr)



# visits_in_rus = []
# for i in geo_logs:
# 	for visit, city in i.items():
# 		if 'Россия'in i[visit]:
# 			visits_in_rus.append(i)
# print(visits_in_rus)