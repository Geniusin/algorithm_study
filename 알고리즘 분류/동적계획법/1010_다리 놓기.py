import sys
input = sys.stdin.readline

def bridg(N, M):
    if N == 1:
        return M

    elif N == M:
        return 1

    elif x[N][M] != 0:
        return x[N][M]

    else:
        for i in range(1, M-N+2):
            x[N][M] += bridg(N-1, M-i)

    return x[N][M]

T = int(input())
results = []

for i in range(T):
    N, M = map(int, input().split())

    x = [[0 for _ in range(M+1)] for _ in range(N+1)]

    results.append(bridg(N, M))

for res in results:
    print(res)
