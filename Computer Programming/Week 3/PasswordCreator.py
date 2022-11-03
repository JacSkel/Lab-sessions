#!/usr/bin/env python3
Bad_passwords = ['Jack', 'Letmein', 'Sesame', 'Hello', 'Password']
flag = False
validity = 0
while flag==0:
    password = input("Enter new password: ")
    password_check = input("Enter password again: ")
    if (len(password)>=8 and len(password)<=12):
        print("Password is Within the character limit")
        validity1=int(validity+1)
    else:
        print("Password is not within the character limit, try again")
        flag==1
    if password in Bad_passwords:
        print("Error password not strong enough, try again")
        flag==1
    else:
        print("Password is a strong password")
        validity2=int(validity+1)
    if password == password_check:
        print("Passwords Matches")
        validity3=int(validity+1)
    else:
        print("Error passwords entered doesn't match, try again")
        flag==1
    if validity1+validity2+validity3==3:
        print("Password set")
    break


