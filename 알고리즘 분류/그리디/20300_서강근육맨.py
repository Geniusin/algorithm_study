import sys
input = sys.stdin.readline

num = int(input())

geun = list(map(int, input().split()))

geun.sort()
res = 0
if len(geun) % 2 == 0:
    for i in range(len(geun) // 2):
        res = max(res, geun[i] + geun[-i-1])

else:
    res = geun[-1]
    for i in range(len(geun) // 2):
        res = max(res, geun[i] + geun[-i-2])

print(res)

