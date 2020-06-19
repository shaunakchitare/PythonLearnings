

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

for item in list(groceries.keys()):
    r = groceries[item]
    if r <= 0:
        del groceries[item]

print(groceries.keys())
print(groceries.values())



