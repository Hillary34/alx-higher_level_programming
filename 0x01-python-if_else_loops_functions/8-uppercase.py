#!/usr/bin/python3
uppercase = __import__('8-uppercase').uppercase

uppercase("Holberton School")
def uppercase(str):
for i in str:
if ord(i) >= 97 and ord(i) <= 122:
i = chr(ord(i) - 32)
print("{}".format(i), end="")
print()
