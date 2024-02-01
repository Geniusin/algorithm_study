# 1463_1로 만들기

import sys

input = sys.stdin.readline

X = int(input())
cnt = 0
while True:
    print(X)
    if X % 3 == 0:
        X = X // 3
    elif X % 2 == 0:
        X = X // 2
    else:
        X -= 1

    cnt += 1
    if X <= 1:
        break
print(cnt)