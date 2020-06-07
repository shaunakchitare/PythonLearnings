
numbers_list = [3,5,23,789,258,12,369,1000,150,5698,8520,100]

for number in numbers_list:
    print(str(number))
    if number < 100:
        print('Below')
    elif number > 100:
        print('Above')
    else:
        print('Same')



