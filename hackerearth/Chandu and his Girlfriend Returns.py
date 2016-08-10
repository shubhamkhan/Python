T = int(input())
N, M =[int(x) for x in input().split()]
A = [N]
B = [M]
C = []
i = 0
while i < T:
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = A + B
    C.sort()
    C.reverse()
    for x in C:
        print(x, end=" ")