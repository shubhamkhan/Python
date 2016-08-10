#!/usr/bin/python/
N = int(input())
A = list()
i = 0
while i < N:
    A.append(int(input()))
    i += 1
for x in A:
    print(x - 1)
