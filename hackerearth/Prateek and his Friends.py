#!/usr/bin/Python/
T = int(input())
k = 0
while k < T:
    N, X = map(int, input().split())
    j = 0
    A = []
    while j < N:
        i = int(input())
        A.append(i)
        j += 1
    k += 1
    q = 0
    cost = 0
    q = A[0] + A[N - 1]
    for l in A:
        cost += l
    cost = cost - q
    if X == cost:
        print("YES")
    else:
        print("NO")