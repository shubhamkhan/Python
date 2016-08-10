#!/usr/bin/python/
l, r, k = map(int, input().split())
count = 0
while l <= r:
    if l % k == 0:
        count = count + 1
    l = l + 1
print(count)
