# 14503 로봇청소기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# R = 7
# C = 4
# D = 0
#
# arr = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]
nD = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 북 동 남 서

cnt = 0
while True:

    if arr[R][C] == 0:
        arr[R][C] = -1
        cnt += 1
    rot = False

    # 주변 4칸 중 청소되는칸 체크
    for d in nD:
        nR = R + d[0]
        nC = C + d[1]

        if arr[nR][nC] == 0:
            rot = True
            break

    if not rot:
        tD = D - 2

        if tD <= -1:
            tD += 4 # 후진(방향 유지)

        nR = R + nD[tD][0]
        nC = C + nD[tD][1]
         # 후진했는데 벽이면 멈춤
        if arr[nR][nC] <= 0:
            R = nR
            C = nC
        else:
            break

    else: # 주변에 청소해야될 곳이 있다?
        D -= 1
        if D == -1:
            D = 3 # 서쪽으로 회전
        nR = R + nD[D][0]
        nC = C + nD[D][1]

        if arr[nR][nC] == 0:
            R = nR
            C = nC


print(cnt)