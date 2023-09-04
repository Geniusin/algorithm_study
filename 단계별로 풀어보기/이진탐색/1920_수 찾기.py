import sys

input = sys.stdin.readline


def bin_search(arr, num, start, end):

    while start <= end:
        mid = (start + end) // 2
        if num == arr[mid]:
            return 1

        elif num > arr[mid]:
            start = mid + 1

        elif num < arr[mid]:
            end = mid - 1

    return 0


N = int(input())
arr_n = list(map(int, input().split()))
arr_n.sort()

M = int(input())
arr_m = list(map(int, input().split()))

start = 0
for i in range(len(arr_m)):
    print(bin_search(arr_n, arr_m[i], start, len(arr_n)-1))

