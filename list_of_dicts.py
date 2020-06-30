

w = {'name':'Shaunak', 'age':8, 'flat':'B506'}
x = {'name':'Kedar', 'age':7, 'flat':'C301'}
y = {'name':'Jas', 'age':9, 'flat':'A401'}

friends = [w, x, y]

#Exercise 1 - search for Kedar in the list and print his flat no
print('\nExercise 1')
for friend in friends:
    if friend['name'] == 'Kedar':
        print(friend['flat'])

#Exercise 2 - print friend names whose age is greater than 7
print('\nExercise 2')
for friend in friends:
    if friend['age']> 7:
        print(friend['name'])

#Exercise 3 - update Shaunak's age to 9 years and print updated age
print('\nExercise 3')
for a_friend in friends:
    if a_friend['name'] == 'Shaunak':
        a_friend['age'] = 9
        print(a_friend['age'])

#Exercise 4 - update Shaunak's name to Kanha and print updated name
print('\nExercise 4')
for a_friend in friends:
    if a_friend['name'] == 'Shaunak':
        a_friend['name'] = 'Kanha'
        print(a_friend['name'])

#Exercise 5 - update Kedar's flat to B505 and print updated flat
print('\nExercise 5')
for a_friend in friends:
    if a_friend['name'] == 'Kedar':
        a_friend['flat'] = 'B506'
        print(a_friend['flat'])

#Exercise 6 - add one name to frinds and print updated
print('\nExercise 6')
z = {'name':'Shrijit', 'age':7, 'flat':'C302'}
friends.append(z)
print(friends)

#Exercise 7 - print 2 frind in frinds
print('\nExercise 7')
print(friends[1])


