
target_list = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

num = 47


start = 0
end = len(target_list)



def bin_search(arr, num, start, end):
    while start >= end:

        mid = (start + end) // 2

        if num == arr[mid]:
            return mid

        elif num > arr[mid]:
            start = mid

        elif num < arr[mid]:
            end = mid
    return None


result = bin_search(target_list, 37, 0, end-1)
print(result)