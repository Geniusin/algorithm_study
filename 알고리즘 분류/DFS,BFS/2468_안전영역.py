import sys
from collections import deque
input = sys.stdin.readline

# 현재 메모리초과 2468_안전영역 -> 방문처리할때 Q에서 pop 할 떄가 아닌 넣을때 해야 한다 (why?)

def dfs(arr, start):

    q = deque([start])


    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    arr[start[0]][start[1]] = True
    while q:
        y, x = q.popleft()
        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if arr[ny][nx] == 1:
                continue
            if arr[ny][nx] == 0:
                arr[ny][nx] = True

                q.append([ny, nx])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

res = 0
max_h = 0
for h in range(0, 101):
    visited = [[False] * N for _ in range(N)]

    for j in range(N):
        for i in range(N):
            if arr[j][i] > max_h:
                max_h = arr[j][i]
            if arr[j][i] <= h:
                visited[j][i] = True

    cnt = 0
    for j in range(N):
        for i in range(N):
            if not visited[j][i]:
                dfs(visited, [j, i])
                cnt += 1
    res = max(cnt, res)

    if max_h <= h:
        break

print(res)