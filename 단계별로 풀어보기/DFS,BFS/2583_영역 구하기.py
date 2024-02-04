# 2583 영역 구하기

import sys
from collections import deque
input = sys.stdin.readline

R, C, K = map(int, input().split())

arr = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    t = y1
    y1 = R - y2
    y2 = R - t

    for i, ar in enumerate(arr[y1:y2]):
        ar[x1:x2] = [1] * (x2-x1)
        arr[y1+i] = ar


visited = [[0 for _ in range(C)] for _ in range(R)]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def bfs(grid):
    q = deque([grid])
    cy, cx = grid
    visited[cy][cx] = True
    size = 1
    while q:
        y, x = q.popleft()

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= R: continue
            if nx < 0 or nx >= C: continue

            if arr[ny][nx] == 0 and visited[ny][nx] == 0:

                visited[ny][nx] = True
                arr[ny][nx] = 1

                q.append([ny, nx])
                size += 1
    return size
cnt = 0

sizes = []
for c in range(C):
    for r in range(R):

        if arr[r][c] == 0 and visited[r][c] == 0:
            s = bfs([r, c])
            sizes.append(s)
            cnt += 1


print(cnt)
sizes.sort()
for s in sizes:
    print(s, end=' ')





