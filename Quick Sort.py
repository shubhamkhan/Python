#!/usr/bin/python/
def partition(arr, beg, end):
    pivot = beg
    for i in range(beg+1, end+1):
        if arr[i] <= arr[beg]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[beg] = arr[beg], arr[pivot]
    return pivot


def qsort(arr, beg=0, end=None):
    if end is None:
        end = len(arr) - 1
    if beg >= end:
        return
    pivot = partition(arr, beg, end)
    qsort(arr, beg, pivot - 1)
    qsort(arr, pivot+1, end)

arr = [97, 200, 100, 101, 211, 107]
qsort(arr)
print(arr)
