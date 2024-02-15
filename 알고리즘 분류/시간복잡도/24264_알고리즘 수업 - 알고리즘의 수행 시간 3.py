n = int(input())


def MOP(num):
    sum = 0
    cnt = 0
    for n in range(1, num + 1):
        for m in range(1, num + 1):
            sum = sum + (n*m)
            cnt += 1
    return cnt

print(n**2)
print(2)