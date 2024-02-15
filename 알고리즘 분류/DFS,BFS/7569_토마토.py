import sys
sys.stdin = open('input.txt', 'r')
#####
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
X = []
# XXX = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
#  [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]

X = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque([])
for z, h in enumerate(X):
    for y, Y in enumerate(h):
        for x, num in enumerate(Y):
            if num == 1:
                queue.append([z, y, x])

move = [[0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]]

date = 0

while queue:
    z, y, x = queue.popleft()

    for m in move:
        nz = z + m[2]
        ny = y + m[1]
        nx = x + m[0]

        if (0 <= ny < N) and (0 <= nx < M) and (0 <= nz < H) and (X[nz][ny][nx] == 0):
            queue.append([nz, ny, nx])
            X[nz][ny][nx] = X[z][y][x] + 1

for k in X:
    for a in k:
        if 0 in a:
            print(-1)
            exit(0)
        date = max(date, max(a))


print(date-1)