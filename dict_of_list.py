

friends = {}
friends['Shaunak'] = ['lego', 'snake and ladder', 'chess', 'x o', 'bear', 'football']
friends['Kedar'] = ['lego', 'x o', 'chess', 'bat', 'ball']
friends['Jas'] = ['lego', 'chess', 'football', 'ball']
friends['Srijit'] = ['lego', 'x o', 'chess', 'magic trick', 'car', 'football', 'bat']

#Exercise 1 - print number of toys for each friend
#Format Shaunak - 6
print('\nExercise 1')
for a_friend in friends:
    toys = friends[a_friend]
    no_of_toys = len(toys)
    print(a_friend + ' - ' + str(no_of_toys))


#Exercise 2 - print names of friends who have 5 or more toys
print('\nExercise 2')
for a_friend in friends:
    toys = friends[a_friend]
    no_of_toys = len(toys)
    if no_of_toys >= 5:
        print(a_friend)

#Exercise 3 - print name of friends who have bat
print('\nExercise 3')
for a_friend in friends:
    toys = friends[a_friend]
    if 'bat' in toys:
        print(a_friend)


#Exercise 4 - add dron to ever one
print('\nExercise 4')
print(a_friend)
for a_friend in friends:
    toys = friends[a_friend]
    toys.append('dron')
    print(' ', toys)


print(friends)

#Exercise 5 - remove chess from ever one
print('\nExercise 5')
for a_friend in friends:
    toys = friends[a_friend]
    if 'chess' in toys:
        toys.remove('chess')
        #i = toys.index('chess')
        #del toys[i]
        print(toys)

#Exercise 6 - remove Shrijit from dict
print('\nExercise 6')
if "Srijit" in friends:
    del friends["Srijit"]

print(" ->" , friends)

#Exercise 7 - remove Shrijit from dict
print('\nExercise 7')
friends['Anvi'] = ['lego', 'snake and ladder', 'chess']
print(friends)

#Exercise 8 - print number of key from friends
print('\nExercise 8')
count = 0
for a_friend in friends:
    count = count + 1

print(count)

print(len(friends))










