#!/usr/bin/python/
L = int(input())
N = int(input())
i = 0
while i < N:
    W, H = map(int, input().split())
    if L > W or L > H:
        print("UPLOAD ANOTHER")
    elif L <= W or L <= H:
        if not H != W:
            print("ACCEPTED")
        elif not W == H:
            print("CROP IT")

    i = i + 1
