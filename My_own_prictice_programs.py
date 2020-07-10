#-------------------------------------------------------------------------------

print('\nExercise 1')
things = ['comb','toytruck','chess','knife','toybear']
for thing in things:
    if 'bomb' in thing:
        break
    else:
        continue
print(things)

#-------------------------------------------------------------------------------

print('\nExercise 2')
for thing in things:
    if 'toytruck'in thing:
        things.remove('toytruck')
print(things)

#-------------------------------------------------------------------------------

print('\nExercise 3')
name = 'Shaunak','jas','kedar','shrijit','anvi'
print(name)

del name

#-------------------------------------------------------------------------------

print('\nExercise 4')
friends = ['vihan','rahul','sneha','kanha','karman','sarasvati']
for friend in friends:
    if 'sarasvati' in friend:
        friends.remove('sarasvati')
        print(friends)
#-------------------------------------------------------------------------------

print('\nExercise 5')
numbers = {'a':1,'b':2,'c':3}
for number in numbers:
    v = numbers[number]
    if 1 == v:
        print('one')

    elif 2 == v:
        print('two')
    elif 3 == v:
        print('three')


#-------------------------------------------------------------------------------

print('\nExercise 6')
nums = [0,1,2,3,4,5,6]
for num in nums:
    if 6 == num:
        print('YES!')
    else:
        print('NO!')

#-------------------------------------------------------------------------------

print('\nExercise 7')
nums = [0,1,2,3,4,5,6]
if 8 in nums:
    print('YES!')
else:
    print('NO!')















