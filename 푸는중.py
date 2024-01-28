# 14503 로봇청소기

import sys

input = sys.stdin.readline

M, N = map(int, input().split())

R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

nD = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 북 동 남 서

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

        if nR < 0 or nR >= N: continue
        if nC < 0 or nC >= M: continue

        if arr[nR][nC] == 0:
            rot = True


            break
    if rot: # 주변에 청소해야될 곳이 있다?

        for _ in range(4):
            D -= 1
            if D == -1: D = 3 # 서쪽으로 회전

            nR = R + nD[D][0]
            nC = C + nD[D][1]

            if nR < 0 or nR >= N: continue
            if nC < 0 or nC >= M: continue

            if arr[nR][nC] == 0:
                arr[nR][nC] = -1 # 청소하면 -1
                R = nR
                C = nC
                cnt += 1
                break
    else:
        D -= 2
        if D <= -1: D += 4 # 후진

        nR = R + nD[D][0]
        nC = C + nD[D][1]
         # 후진했는데 벽이면 멈춤
        if nR <= 0 or nR >= N: break
        if nC <= 0 or nC >= M: break

        R = R + nD[D][0]
        C = C + nD[D][1]

print(cnt)