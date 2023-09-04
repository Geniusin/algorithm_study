import sys

input = sys.stdin.readline

N = input()[:-1]



x = 0
for n in N:
    x += int(n)

M = int(N) + x