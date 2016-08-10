#!/usr/bin/python/
T = int(input())
i = 0
A = []
while i < T:
    N = int(input())
    A = [int(x) for x in input().split()]
    cnt = len(A)
    if N == cnt:
        A.sort()
        A.reverse()
        for x in A:
            print(x, end=" ")
        print()
    i += 1