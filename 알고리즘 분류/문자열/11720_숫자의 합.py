import sys
input = sys.stdin.readline

N = int(input())

num = input()

x = 0
for n in num[:-1]:
    x += int(n)

print(x)