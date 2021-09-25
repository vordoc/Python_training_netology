ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique_ids = set()
for values_1 in ids.values():
	for numbers in values_1:
		unique_ids.add(numbers)
print(list(unique_ids))