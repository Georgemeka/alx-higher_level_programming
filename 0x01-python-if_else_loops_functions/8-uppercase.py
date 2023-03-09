#!/usr/bin/python3
def uppercase(str):
    strg = ""

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            t = chr(ord(i) - 32)
        else:
            t = i
        strg = strg + t


print("{}".format(strg))
