import sys
from collections import deque

input = sys.stdin.readline

def bfs(grid):
    size = 1
    q = deque([grid])
    cy, cx = grid
    visited[cy][cx] = True
    while q:

        r, c = q.popleft()
        for i in range(4):
            ny = r + dy[i]
            nx = c + dx[i]

            if ny < 0 or ny >= R: continue
            if nx < 0 or nx >= C: continue

            if visited[ny][nx] == 0 and arr[ny][nx] == 1:
                visited[ny][nx] = True
                q.append([ny, nx])
                size += 1

    return size

R, C = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

max_size = 0
cnt_img = 0
for r in range(R):
    for c in range(C):
        if arr[r][c] != 0 and visited[r][c] == 0:
            max_size = max(max_size, bfs([r, c]))
            cnt_img += 1

if cnt_img == 0:
    max_size = 0

print(cnt_img)
print(max_size)
