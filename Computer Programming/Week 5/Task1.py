#!/usr/bin/env python3

if __name__ == '__main__':
    name = input("Greetings! How shall we call you? ")
    title = ["Lord", "Lady"]
    x = name[0:4]
    if x in title:
        print("It shall be so, ", name)
    else:
        print("You man not be known by that name!")