import sys

input = sys.stdin.readline

P = input()[:-1]
S = input()[:-1]

if S in P:
    print(1)
else:
    print(0)