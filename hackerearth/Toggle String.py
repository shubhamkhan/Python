#!/usr/bin/python/
import sys
S = list(input())
for x in S:
    if x.isupper():
        print(x.lower(), end="")
    elif x.islower():
        print(x.upper(), end="")