import sys
input = sys.stdin.readline

def is_sosu(num):


    if num == 1:
        return 0

    if num == 2 or num == 3:

        return 1
    prime = 1
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            prime = 0
            break

    return prime


N = int(input())
nums = list(map(int, input().split()))
x = 0
for i in nums:
    res = is_sosu(i)
    x += res
print(x)