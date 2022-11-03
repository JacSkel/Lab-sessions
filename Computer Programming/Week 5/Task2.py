#!/usr/bin/env python3

num_spam = int(input("How many slices of spam? "))

if num_spam == 1:
    print("Egg with Spam coming up!")
else:
    num_spam_sub = num_spam - 1
    spam_check = str("Spam, ") * num_spam_sub
    print("Egg with",spam_check + "and Spam coming up!")

