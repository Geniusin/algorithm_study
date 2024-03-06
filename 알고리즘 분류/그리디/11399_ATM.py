import sys
input = sys.stdin.readline


N = int(input())

times = list(map(int, input().split()))

times.sort()


total_time = 0
tmp = 0
for time in times:
    tmp += time
    total_time += tmp

print(total_time)