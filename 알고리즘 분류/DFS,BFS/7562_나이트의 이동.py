# 7562_나이트의 이동

import sys
from collections import deque


T = int(input())


move = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]

def bfs(start):

    q = deque([start])

    while q:

        r, c = q.popleft()
        for i in range(8):

            nr = r + move[i][0]
            nc = c + move[i][1]

            if nr >= 0 and nr < I and nc >= 0 and nc < I and arr[nr][nc] == 1:

                arr[nr][nc] = arr[r][c] + 1

                if (nr, nc) == end:
                    break


                q.append([nr, nc])


for _ in range(T):

    I = int(input())

    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    if start == end:
        print(0)
    else:

        arr = [[1 for _ in range(I)] for _ in range(I)]

        bfs(start)

        print(arr[end[0]][end[1]]-1)