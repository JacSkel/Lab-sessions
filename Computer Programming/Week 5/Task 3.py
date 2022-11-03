#!/usr/bin/env python3

flag = False
while flag == 0:
    password_check = ("parrot")
    password = input("Greetings! What is the password? ")
    if password == password_check:
        print("Correct! You may enter.")
        flag == 1
        break
    else:
        print("Incorrect! You may try again")