import sys
input = sys.stdin.readline

S = input()[:-1]

start = S[0]

togle = 0
for c in S:

    if start != c:
        start = c
        togle += 1

if togle % 2 == 0:
    print(togle // 2)
else:
    print((togle+1) // 2)