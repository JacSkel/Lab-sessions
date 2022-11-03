#!/usr/bin/env python3

name = input("Hello, what is your name? ")

if not name:
    print("Hello, Stranger!")
else:
    print(f"Hello, {name}!")

print(f"Hello, {name if name else 'Stranger'}!")

