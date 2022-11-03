#!/usr/bin/env python3

if __name__ == '__main__':
    Number = int(input("Enter a number to see if it is in range? "))
    if Number in range(100):
        print ("True")
    else:
        print ("False")