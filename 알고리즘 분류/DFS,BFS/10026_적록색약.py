# 10026 적룍색약

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

arr = [input()[:-1] for _ in range(N)]
"R-G" "B"

visited = [[0] * N for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(grid, is_color):

    q = deque([grid])
    visited[grid[0]][grid[1]] = 1
    while q:
        y, x = q.popleft()

        cur = arr[y][x]


        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N: continue
            if nx < 0 or nx >= N: continue
            if visited[ny][nx] != 0: continue

            if is_color:
                if cur == arr[ny][nx]:
                    q.append([ny, nx])
                    visited[ny][nx] = 1

            else:
                if cur == 'B':
                    if cur == arr[ny][nx]:
                        q.append([ny, nx])
                        visited[ny][nx] = 1
                else :
                    if arr[ny][nx] != 'B':
                        q.append([ny, nx])
                        visited[ny][nx] = 1
cnt = 0
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            bfs([r, c], True)
            cnt += 1


cnt_new = 0
visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            bfs([r, c], False)
            cnt_new += 1

print(cnt, cnt_new)