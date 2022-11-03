#!/usr/bin/env python3
number = int(input("Enter a number for its multiples? "))
numbers_valid = [0,1,2,3,4,5,6,7,8,9,10,11,12]
backwards_number = [-0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12]
if number in backwards_number:
    for n in range(13-0):
        print(n, 'x', number, '=', n * number)
else:
    print("Enter a valid number")
if number in numbers_valid:
    for n in range(13):
        print(n,'x',number,'=',n*number)
else:
    print("Enter a valid number")