import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    R, S = input().split()
    x = ''
    for s in S:
        for r in range(int(R)):
            x += s

    print(x)