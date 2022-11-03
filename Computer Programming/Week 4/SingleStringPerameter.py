#!/usr/bin/env python3

str_obj = str(input("Enter a word?"))
count_upper = sum(1 for elem in str_obj if elem.isupper())
count_lower = sum(1 for elem in str_obj if elem.islower())
print(count_upper,"Upper characters in the string")
print(count_lower,"Lower characters in the string")



