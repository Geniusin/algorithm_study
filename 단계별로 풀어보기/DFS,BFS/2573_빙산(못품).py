# 2573_빙산

import sys
import copy
from collections import deque

input = sys.stdin.readline


def bfs(grid):
    q = deque([grid])
    while q:
        r, c = q.popleft()

        for i in range(4):
            ny = r + dy[i]
            nx = c + dx[i]


            if ny < 0 or ny >= R: continue
            if nx < 0 or nx >= C: continue

            if visited[ny][nx] == 0:

                if arr[ny][nx] != 0:
                    q.append([ny, nx])
                    visited[ny][nx] = 1

R, C = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

time = 0

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while True:
    # 빙산 수 체크를 위한 임시 arr
    _arr = copy.deepcopy(arr)

    # bfs를 이용한 빙산 수 체크
    mess = 0
    visited = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c] != 0:
                bfs([r, c])

                mess += 1

    # 빙산이 두 조각으로 나뉘었다면 루프 종료
    if mess >= 2:
        break

    check = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):

            if arr[r][c] > 0:

                num_0 = 0
                for i in range(4):

                    ny = r + dy[i]
                    nx = c + dx[i]

                    if ny < 0 or ny >= R: continue
                    if nx < 0 or nx >= C: continue

                    if arr[ny][nx] == 0:
                        check[r][c] += 1

    for r in range(R):
        for c in range(C):
            arr[r][c] -= check[r][c]

            if arr[r][c] < 0:
                arr[r][c] = 0

    # 빙산이 나뉘지 않고 전부 물에 잠긴경우
    if sum([sum(arr_r) for arr_r in arr]) == 0:
        time = 0
        break

    time += 1

print(time)