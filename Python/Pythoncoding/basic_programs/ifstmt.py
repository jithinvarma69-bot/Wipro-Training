"""
Date: 24-04-2026
"""
#big2
'''
num1 = int(input('Enter a number'))
num2 = int(input('Enter another number'))

if num1 > num2:
    print(num1, ' is big.')
else:
    print(num2, ' is big.')
'''


#big3
'''
num1 = int(input('Enter a number'))
num2 = int(input('Enter another number'))
num3 = int(input('Enter another number'))

if num1 == num2 and num2 == num3:
    print('All values are equal')
elif num1 > num2 and num1 > num3:
    print(num1, ' num1 is biggest')
elif num2 > num1 and num2 > num3:
    print(num2, ' num2 is biggest')
elif num3 > num2 and num3 > num1:
    print(num3, ' num3 is biggest')
'''

#Weekday

ch = int(input('Enter a number bet 1-7'))

match ch:
    case 1:
        print('Mon')
    case 2:
        print('Tue')
    case 3:
        print('Wend')
    case 4:
        print('Thurs')
    case 5:
        print('Fri')
    case 6:
        print('Sat')
    case 7:
        print('Sun')
    case _:
        print('invalid choice')











