list_1 = ['2018-01-01', 'yandex', 'cpc', 100]

dict_1 = {list_1[-2]: list_1[-1]}
# print(dict_1)
for i in list_1[:-2][::-1]:
    dict_1 = {i: dict_1}
    # print(i)
print(dict_1)