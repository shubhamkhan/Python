#!/usr/bin/python
import string
N = input()
N = N.casefold()
RN = reversed(N)
if list(N) == list(RN):
    print("YES")
else:
    print("NO")