

groceries = {}
groceries['rice'] = 2
groceries['tomato'] = 5
groceries['mango'] = 1
groceries['banana'] = 1
groceries['strawberry'] = 5


for item in groceries:
    r = groceries[item]
    r = r + 1
    groceries[item] = r

for item in groceries:
    r = groceries[item]
    r = r - 2
    groceries[item] = r


print(groceries.keys())
print(groceries.values())



