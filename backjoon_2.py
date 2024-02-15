# 알고리즘 분류 (1차원배열) - 10807 개수 세기

N = int(input())

nums = map(int, input().split())

target = int(input())

cnt = 0
for num in nums:
    if num == target: cnt += 1

print(cnt)

# 10810 공 넣기
N, M = map(int, input().split())
list_n = [0 for x in range(N)]
for n in range(M):
    i, j, k = map(int, input().split())

    for x in range(i, j+1):
     list_n[x-1] = k
a = ''
for o in list_n:
    a += ' ' +str(o)
print(a[1:])

# 10813 공 바꾸기

N, M = map(int, input().split())
list_n = [x+1 for x in range(N)]

for n in range(M):
    i, j = map(int, input().split())


    tmp = list_n[i-1]
    list_n[i-1] = list_n[j-1]
    list_n[j-1] = tmp

a = ''
for o in list_n:
    a += ' ' +str(o)
print(a[1:])

# 5597번 과제 안 내신분?

x = [i for i in range(1, 31)]
for i in range(28):
    n = int(input())

    x.remove(n)

for res in x:
    print(res)


# 3052 나머지

x = list()
for i in range(10):
    n = int(input())

    k = n % 42
    if k not in x: x.append(k)


print(len(x))


# 10811 바구니 뒤집기
N, M = map(int, input().split())

baskets = [n+1 for n in range(N)]

for n in range(M):
    i, j = map(int, input().split())
    tmp = baskets[i-1: j]
    t = tmp[::-1]
    cnt = 0
    for k in range(i-1, j):
        baskets[k] = t[cnt]
        cnt += 1

a = ''
for o in baskets:
    a += ' ' +str(o)
print(a[1:])

# 1546 평균

N = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)
new_scores = []
for score in scores:
    new_score = score / max_score * 100
    new_scores.append(new_score)

print(sum(new_scores) / len(new_scores))