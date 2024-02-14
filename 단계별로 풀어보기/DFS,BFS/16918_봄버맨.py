# 16918 봄버맨

import sys
import copy
from collections import deque

input = sys.stdin.readline

R, C, N = map(int, input().split())

t_arr = [input().split() for _ in range(R)]
arr = []
for ar in t_arr:
    arr.append([*ar[0]])


def bfs(grid):
    q = deque([grid])

    visited[grid[0]][grid[1]] = '.'

    while q:

        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= R: continue
            if nx < 0 or nx >= C: continue

            if visited[ny][nx] == 'O':
                visited[ny][nx] = '.'


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

if N == 1:
    pass
elif N % 2 == 0:
    arr = [['O'] * C for _ in range(R)]

else:
    for t in range(N//2):

        visited = [['O'] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if arr[r][c] == 'O':
                    bfs([r, c])

        arr = copy.deepcopy(visited)

for ar in arr:
    print(''.join(ar))
