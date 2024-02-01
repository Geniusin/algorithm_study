import sys
from collections import deque


T = int(input())

def bfs(start):

    q = deque([start])

    while q:

        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= 0 and ny < R and nx >= 0 and nx < C:

                if arr[ny][nx] > 0:
                    arr[ny][nx] = -1

                    q.append([ny, nx])




dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for _ in range(T):
    R, C, K = map(int, input().split())

    arr = [[0 for _ in range(C)] for _ in range(R)]

    for _ in range(K):
        y, x = map(int, input().split())

        arr[y][x] = 1
    cnt = 0
    for r in range(R):
        for c in range(C):

            if arr[r][c] > 0:
                bfs([r, c])
                cnt += 1

    print(cnt)
