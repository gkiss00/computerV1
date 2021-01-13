from cmath import *
import unittest

#print('\u00B2')

def main():
    final = []
    sign = []
    stri = "-"
    args = stri.split("+")
    for i in range(len(args)):
        a = args[i].split("-")
        for j in range(len(a)):
            final.append(a[j])
    sign.append(0)
    for i in range(len(stri)):
        if stri[i] == '-':
            sign.append(-1)
        if stri[i] == '+':
            sign.append(1)
    print(final)
    print(sign)
    

main()