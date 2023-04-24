
# Level2 최대값과 최솟값
def solution(s):
    list_s = s.split()

    tmp = []
    for i in list_s:
        tmp.append(int(i))
    answer = f'{min(tmp)} {max(tmp)}'
    return answer


# Level 2 끝말잇기
def solution(n, words):

    words_list = list()
    FLAG = True
    for i, word in enumerate(words):

        man_num = (i+1) % n
        if man_num == 0: man_num = n
        try_num = (i // n) + 1

        if word not in words_list:
            words_list.append(word)
        else:
            FLAG = False
            break

        if i>= 1:
            if words_list[i][0] != words_list[i-1][-1]:
                FLAG = False
                break
    if FLAG:
        answer = [0, 0]
    else:
        answer = [man_num, try_num]

    return answer

words = ["hello", "one", "even", "never", "now", "world", "draw", "hello"]
n = 3
print(solution(n, words))


cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cacheSize = 5

run_time = 0
caches = []
for city in cities:
    city_low = city.lower()

    if city_low in caches:
        run_time += 1
        caches.remove(cities)
        caches.append(city_low)
    else:
        run_time += 5
        caches.append(city_low)
        if len(caches) > cacheSize: del caches[0]


import re

str1 = 'aa1+aa2'
str2 = 'AAAA12'

p = re.compile('[a-zA-Z]')
nump = re.compile('[0-9]')
list_char1 = []
len_str1 = len(str1)
for num in range(0, len_str1 - 1):
    char1 = str1[num: num + 2]
    if ' ' in char1: continue
    m1 = p.match(char1)
    m2 = nump.match(char1)
    if m1 : list_char1.append(char1.lower())

list_char2 = []
len_str2 = len(str2)
for num2 in range(0, len_str2 - 1):
    char2 = str2[num2: num2 + 2]
    if ' ' in char2: continue
    m1 = p.match(char2)
    m2 = nump.match(char2)
    if m1 and (m2 == None): list_char2.append(char2.lower())

set_char1 = set(list_char1)
set_char2 = set(list_char2)

inter = set_char1 & set_char2
union = set_char1 | set_char2



answer = len(inter) / len(union) * 65536
