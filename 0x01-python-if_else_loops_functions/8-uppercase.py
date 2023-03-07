#!/usr/bin/python3
def uppercase(str):
    strr = list(str)
    for i in range(len(str)):
        if (ord(str[i]) >= 95) and (ord(str[i]) <= 122):
            strr[i] = chr(ord(str[i]) - 32)
    str = "".join(strr)
    print("{}".format(str))
