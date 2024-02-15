import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input()[:-1])))


start = [0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(graph, start):

    queue = deque()
    queue.append(start)

    while queue:
        y, x = queue.popleft()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue

            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny, nx])

    return graph[N-1][M-1]

print(bfs(graph, start))