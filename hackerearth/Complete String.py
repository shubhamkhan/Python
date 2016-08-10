#!/usr/bin/python/
N = int(input())
for num in range(N):
    A = set()
    str = input().lower()
    for ch in str:
        A.add(ch)
    f = True
    char = 'a'
    for i in range(26):
        char = chr(ord('a') + i)
        if char not in A:
            f = False
            break
    if f == True:
        print('YES')
    else:
        print('NO')
    num += 1