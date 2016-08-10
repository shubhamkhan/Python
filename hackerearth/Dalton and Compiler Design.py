#!/usr/bin/python/
T = int(input())
i = 0
while i < T:
    n = int(input())
    p = int(n / 2)
    print(p, end=" ")
    print(n - p)
    i = i + 1