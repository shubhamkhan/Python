#!/usr/bin/python/
i = 0
N = list()
while (i < 10) :
    N.append(int(input()))
    if N[i] == 42:
        N.append(int(input()))
        break
    else:
        i = i + 1
for x in range(len(N)):
    if N[x+1] < N[x] :
        print(N[x])
        break
    else:
        print(N[x])
