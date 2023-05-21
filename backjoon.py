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

# 14501