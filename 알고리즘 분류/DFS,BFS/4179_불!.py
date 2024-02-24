# 5427 불

import sys
from collections import deque

def fire(grid):

    q = deque([grid])
    while q:

        y, x = q.popleft()

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= R: continue
            if nx < 0 or nx >= C: continue

            if new_arr[ny][nx] == '.' or new_arr[ny][nx] == 'J':
                new_arr[ny][nx] = 'F'
                fire_locs.append([ny, nx])


def dog(grid):

    q = deque([grid])
    move = False
    while q:

        y, x = q.popleft()

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= R: continue
            if nx < 0 or nx >= C: continue

            if new_arr[ny][nx] == '.':
                new_arr[ny][nx] = 'J'
                move = True
                jihoon_locs.append([ny, nx])
    return move

input = sys.stdin.readline


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


R, C = map(int, input().split())

arr = [input()[:-1] for _ in range(R)]

time = 0
new_arr = [[c for c in ar] for ar in arr]

jihoon_locs = deque()
fire_locs = deque()
is_escape = False
is_break = False

for r in range(R):
    for c in range(C):
        if new_arr[r][c] == 'J':
            jihoon_locs.append([r, c])
        if new_arr[r][c] == 'F':
            fire_locs.append([r, c])

while True:

    len_fire = len(fire_locs)
    for _ in range(len_fire):
        fire_loc = fire_locs.popleft()
        fire(fire_loc)

    moves = []
    len_dog = len(jihoon_locs)
    for _ in range(len_dog):
        r, c = jihoon_locs.popleft()
        if r <= 0 or r >= (R - 1) or c <= 0 or c >= (C-1):
            is_escape = True
            is_break = True
            break

        moves.append(dog([r, c]))

    time += 1

    if sum(moves) <= 0:
        is_break = True

    if is_break:
        break

if is_escape:
    print(time)
else:
    print("IMPOSSIBLE")