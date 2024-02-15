# 2573_빙산
import sys
import copy
from collections import deque

input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(grid):
    q = deque([grid])

    while q:
        r, c = q.popleft()

        num_melt = 0
        for i in range(4):

            ny = r + dy[i]
            nx = c + dx[i]

            if ny < 0 or ny >= R: continue
            if nx < 0 or nx >= C: continue

            if visited[ny][nx] == 0:
                    if arr[ny][nx] != 0:
                        q.append([ny, nx])
                        visited[ny][nx] = 1
                        grids.append([ny, nx])
                    else:
                        num_melt += 1

        melted[r][c] = num_melt

year = 0
while True:

    visited = [[0] * C for _ in range(R)]
    melted = [[0] * C for _ in range(R)]


    cnt_ice = 0
    grids = []
    for r in range(R):
        for c in range(C):
            if arr[r][c] != 0 and visited[r][c] == 0:
                bfs([r, c])
                cnt_ice += 1

    if cnt_ice >= 2:
        break

    for g in grids:
        r, c = g[0], g[1]
        if melted[r][c] != 0:
            arr[r][c] = arr[r][c] - melted[r][c]

            if arr[r][c] < 0:
                arr[r][c] = 0
    #
    # for r in range(R):
    #     for c in range(C):
    #         if melted[r][c] != 0:
    #             arr[r][c] = arr[r][c] - melted[r][c]
    #
    #             if arr[r][c] < 0:
    #                 arr[r][c] = 0

    if sum([sum(arr_r) for arr_r in arr]) == 0:
        year = 0
        break

    year += 1

print(year)
