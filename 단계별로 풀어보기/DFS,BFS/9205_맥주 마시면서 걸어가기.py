import sys
from collections import deque


input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())  # 편의점 개수


    start = tuple(map(int, input().split()))
    stores = []

    for i in range(N):
        stores.append(tuple(map(int, input().split())))
    e_y, e_x = map(int, input().split())

    q = deque([start])
    beers = 20
    visited = [0 for _ in range(len(stores))]

    is_arrival = False
    while q:
        c_y, c_x = q.popleft()

        if (abs(e_y - c_y) + abs(e_x - c_x)) / 50 <= 20:
            is_arrival = True
            break

        for i, store in enumerate(stores):
            t_y, t_x = store

            if visited[stores.index(store)] == 0:
                if (abs(c_y - t_y) + abs(c_x - t_x)) / 50 <= 20:

                    q.append((t_y, t_x))
                    visited[stores.index(store)] = 1
                    beers = 20


    if is_arrival:
        print("happy")
    else:
        print("sad")
