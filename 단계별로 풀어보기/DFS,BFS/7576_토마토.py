import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
X = []

for n in range(N):
    X.append(list(map(int, input().split())))

move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

flag =True
date = 0

# 1 전체 그래프를 만들고

changed = False
while flag:
    tmp = True
    recent = []
    for y, n in enumerate(X):
        for x, m in enumerate(n):
            if X[y][x] == 1 and [y, x] not in recent:

                for m in move:
                    ny = y + m[1]
                    nx = x + m[0]

                    if (0 <= ny < N) and (0 <= nx < M) and (X[ny][nx] == 0):
                        recent.append([ny, nx])
                        X[ny][nx] = 1
                        tmp = False
                        changed = True

    if tmp:
        break
    date += 1

if not changed:
    print(0)
else:

    for a in X:
        for b in a:
            if b == 0:
                date = -1


    print(date)


###########

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
X = []

# for n in range(N):
#     X.append(list(map(int, input().split())))
X = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
for y, Y in enumerate(X):
    for x, num in enumerate(Y):
        if num == 1:
            queue.append([y, x])

move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

date = 0

while queue:
    y, x = queue.popleft()

    for m in move:
        ny = y + m[1]
        nx = x + m[0]

        if (0 <= ny < N) and (0 <= nx < M) and (X[ny][nx] == 0):
            queue.append([ny, nx])
            X[ny][nx] = X[y][x] + 1

for a in X:
    for b in a:
        if b == 0:
            print(-1)
            exit(0)
    date = max(date, max(a))


print(date-1)