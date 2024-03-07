import sys
input = sys.stdin.readline

num_pblm = int(input())

colors = input()[:-1]

num_B = 0
num_R = 0

start = colors[0]
if start == 'R': num_R += 1
if start == 'B': num_B += 1
cnt = 1
for color in colors[1:]:

    if start != color:
        if color == 'R': num_R += 1
        if color == 'B': num_B += 1
        start = color
        cnt += 1

print(min(cnt, (min(num_B, num_R) + 1)))