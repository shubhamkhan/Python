#!/usr/bin/python/
T = int(input())
i = 0
while i < T:
    mbox = 0
    N = int(input())
    A = [int(x) for x in input().split()]
    for x in A:
        if x % 2 != 0:
            #print(mbox)
            mbox += 1
        else:
            mbox += x
    print(mbox)
    i += 1