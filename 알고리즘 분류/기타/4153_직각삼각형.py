import sys

input = sys.stdin.readline

tri_list = []
while True:
    tri = list(map(int, input().split()))
    if tri == [0, 0, 0]:
        break

    else:
        tri.sort()
        tri_list.append(tri)

for tri in tri_list:

    max_num = tri[2] ** 2

    if tri[0] ** 2 + tri[1] ** 2 == max_num:
        print('right')
    else:
        print('wrong')