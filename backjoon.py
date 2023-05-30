# 13458

num_space = int(input())
num_person = list(map(int, input().split()))

main_cnt, sub_cnt = map(int, input().split())


count = 0
for i in num_person:
    if i >= main_cnt:
        count += 1 # main

        if ((i - main_cnt) % sub_cnt) == 0:
            count += ((i - main_cnt) // sub_cnt)

        else:
            count += ((i - main_cnt) // sub_cnt) + 1

    else:
        count += 1

print(count)

# 15721 번데기

num = int(input())

count = int(input())

bbun = int(input())

num = 4
count = 6

list_person = [0 for i in range(count)]
re = 2
for i, per in enumerate(range(count)):

    if i < 4:
        if i % 2 == 0:
            list_person[i] = 0
        elif i % 2 == 1:
            list_person[i] = 1



n = 10
def sum(n):
    x = 0
    for i in range(1, n+1):
        x += i
    return x

print(sum(n))

def recursive_sum(n):
    if n == 1: return 1

    return n + recursive_sum(n-1)


print(recursive_sum(n))


x = []
for i in range(1, 4):
    for j in range(2, 5):
        for k in range(3, 6):
            if (i >= j) or (j >= k) or (i >= k):
                continue
            x.append([i, j, k])

            print([i, j, k])
print(x)


def comb(n, r):
    x = [i for i in range(n)]
    tmp = []

    small_num = x.pop(0)
    for num in x:
        tmp.append([small_num, num])
    return tmp



print(comb(4, 2))

