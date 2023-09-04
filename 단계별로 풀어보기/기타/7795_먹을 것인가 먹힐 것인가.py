import sys
input = sys.stdin.readline

T = int(input())

cnt_list = list()
for i in range(T):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0

    for a_num in A:
        for b_num in B:
            if a_num > b_num:
                cnt += 1

    cnt_list.append(cnt)

for num in cnt_list:
    print(num)