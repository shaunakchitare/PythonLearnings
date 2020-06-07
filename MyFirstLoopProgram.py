fruits_list = ['Pinapple', 'Banana', 'Chiku','Mango','Guava', 'Orange', 'Grapes']

fruits_i_like = ['Mango','Grapes','Chiku']

for fruit in fruits_list:
    #if fruit == 'Mango'or fruit == 'Grapes' or fruit == 'Chiku':
    if fruit in fruits_i_like:
        print('I love it')
    else:
        print('Ok ok')