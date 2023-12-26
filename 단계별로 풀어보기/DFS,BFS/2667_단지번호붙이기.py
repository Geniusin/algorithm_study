import sys
input = sys.stdin.readline

N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, input()[:-1])))

def dfs(graph, start, danji):

    y, x = start

    if y < 0 or x < 0 or y >= N or x >= N:
        return False


    if graph[y][x] == 1:
        graph[y][x] = danji

        dfs(graph, [y+1, x], danji)
        dfs(graph, [y-1, x], danji)
        dfs(graph, [y, x-1], danji)
        dfs(graph, [y, x + 1], danji)

        return True

    return False

result = 0
danji = 2
for i in range(N):
    for j in range(N):
        if graph[j][i] == 1:
            if dfs(graph, [j, i], danji) == True:
                result += 1
                danji += 1

from collections import Counter
counter = Counter()

for i in graph:
    for j in i:
        if j != 0:
            counter.update([j])

print(result)
x = list(counter.values())
x.sort(reverse=False)
for v in x:
    print(v)



# BFS 풀이

import sys
input = sys.stdin.readline

N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, input()[:-1])))


from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(graph, start, c):

    queue = deque()

    queue.append(start)

    while queue:

        y, x = queue.popleft()
        graph[y][x] = c
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[ny][nx] == 1:
                queue.append([ny, nx])



c = 2
results = 0
for i in range(N):
    for j in range(N):
        if graph[j][i] == 1:
            bfs(graph, [j, i], c)
            c += 1

from collections import Counter
counter = Counter()

for i in graph:
    for j in i:
        if j != 0:
            counter.update([j])

print(results)
x = list(counter.values())
x.sort(reverse=False)
for v in x:
    print(v)

