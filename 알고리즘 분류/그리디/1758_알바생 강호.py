import sys
input = sys.stdin.readline

N = int(input())

tips = [int(input()) for _ in range(N)]
tips.sort(reverse=True)
total_tips = 0
for i in range(N):
    cost = tips[i] - i

    if cost <= 0:
        pass
    else:
        total_tips += cost


print(total_tips)
