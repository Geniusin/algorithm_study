# 1517 버블 소트

import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))


cnt = 0
while True:
    flag = False
    for i in range(len(arr)-1):

        if arr[i] > arr[i+1]:

            t = arr[i]

            arr[i] = arr[i+1]
            arr[i+1] = t
            cnt += 1
            flag = True

    if flag == False:
        break

print(cnt)