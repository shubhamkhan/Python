#!/usr/bin/python/
N = int(input())
A = list(map(int, input().split()))
answer = 1
for i in A:
    answer = (i * answer) % (10**9 + 7)
print(answer)