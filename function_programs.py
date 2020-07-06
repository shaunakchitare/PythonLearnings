#-------------------------------------------------------------------------------
#Exercise 1 - Creat a function that accepts 3 ardument and return their sum
print('\nExercise 1')
def add_numbers(x,y,z):
    total = x + y + z
    return total

total = add_numbers(5,1,9)
print(total)
#-------------------------------------------------------------------------------
#Exercise 2 - Create a
print('\nExercise 2')
def add_numbers_2(list_nums):
    total = 0
    for num in list_nums:
        total = total + num

    return total


total = add_numbers_2([4,3,7,5,8])
print(total)
#-------------------------------------------------------------------------------
print('\nExercise 3')
def add_numbers_3(list_nums_1,list_nums_2):
    list_nums = list_nums_1 + list_nums_2

    return add_numbers_2(list_nums)

total = add_numbers_3([4,3,7,5,8],[5,7,6,1,4])
print(total)

#-------------------------------------------------------------------------------
print('\nExercise 4')
def add_numbers_4(list_nums_1,list_nums_2,list_nums_3):
    list_nums = list_nums_1 + list_nums_2 + list_nums_3

    return add_numbers_2(list_nums)


total = add_numbers_4([4,3,7,5,8],[5,7,6,1,4],[9,5,7,0,2])
print(total)

#-------------------------------------------------------------------------------
print('\nExercise 5')
def add_numbers_5(my_dict):
    v1 = my_dict['a']
    v2 = my_dict['b']
    v3 = my_dict['c']
    L1 = [v1,v2,v3]
    r = sum(L1)
    return r

total = add_numbers_5({'a':1,'b':2,'c':3})
print(total)

#-------------------------------------------------------------------------------
print('\nExercise 6')
def add_numbers_6(my_dict):
    values = my_dict.values()
    r = sum(values)
    return r

total = add_numbers_6({'a':1,'b':2,'c':3, 'd':4})
print(total)








