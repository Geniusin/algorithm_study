import sys
input = sys.stdin.readline


N, M = map(int, input().split())

X = []
for n in range(M):
    X.append(list(map(int, input().split())))
