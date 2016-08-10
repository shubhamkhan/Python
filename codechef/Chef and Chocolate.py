#!/usr/bin/python/
T = int(input())
i = 0
while i < T:
    n, m = map(int, input().split())
    if (n + m) % 2 != 0:
        print("Yes")
    else:
        print("No")
    i += 1