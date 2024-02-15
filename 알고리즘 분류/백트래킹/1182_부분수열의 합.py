# 1182 부분수열의 합

# 부분수열은 연속적이지 않아도 됨됨
import sys

input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0
slice_len = 1
for _ in range(N):
    start = 0

    arr_len = len(arr) - slice_len + 1
    for i in range(arr_len):
        sub_arr = arr[start:start+slice_len]
        print(sub_arr)
        res = sum(sub_arr)

        if res == S:
            cnt += 1

        start += 1


    slice_len += 1
print(cnt)





#