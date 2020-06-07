#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Laxmikant
#
# Created:     16/05/2020
# Copyright:   (c ) Laxmikant 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def check_odd_or_even(num):
    remainder = num%2
    if remainder == 1:
        print('Odd number')
    else:
        print('Even number')


def main():
    check_odd_or_even(1357)

if __name__ == '__main__':
    main()
