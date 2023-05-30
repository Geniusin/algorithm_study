alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N',
              'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def make_dict(alphas):
    alpa_dict = dict()
    for i in range(26):
        alpa_dict[alphas[i]] = i+1

    return alpa_dict
count = len(alpha_list) + 1
dict_res = make_dict(alphas=alpha_list)

msg = 'KAKAO'
len_msg = len(msg)
result = []
for i in range(len_msg + 1):

    for j in range(i + 1, len_msg + 1):
        search_word = msg[i:j]
        if search_word in alpha_list:
            result.append(dict_res[search_word])
        else:
            alpha_list.append(search_word)
            dict_res[search_word] = count
            result.append(dict_res[search_word])
            count += 1
            break

for res in result:
    print(res)

# 다트
def solution(dartResult):

    bonuses = ['S', 'D', 'T']
    options = ['*', '#']
    scores = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    tmp = '10'

    tmp_list = []
    cnt = 0
    for n in range(len(dartResult) - 1):
        a = dartResult[n:n + 2]

        if a == tmp:
            tmp_list.append(a)
            cnt += 1
        else:
            if cnt == 0:
                tmp_list.append(a[0])
                tmp_list.append(a[1])
                cnt += 1
            else:
                tmp_list.append(a[-1])
                cnt += 1

    scores_list = list()
    i = 0
    tmp_score = 0
    print(tmp_list)
    for char in tmp_list:
        if char in scores:
            tmp_score = int(char)
            continue
        if char in bonuses:
            if char == 'S':
                scores_list.append(tmp_score)
                i += 1
                continue
            elif char == 'D':
                scores_list.append(tmp_score ** 2)
                i += 1
                continue
            elif char == 'T':
                scores_list.append(tmp_score ** 3)
                i += 1
                continue
        if char in options:
            if char == '*':
                if i == 1:
                    scores_list[i - 1] *= 2
                else:
                    scores_list[i - 1] *= 2
                    scores_list[i - 2] *= 2
            if char == '#':
                scores_list[i - 1] *= -1

    answer = sum(scores_list)

    return answer


a = solution("10D4S10D")

# 보물지도

x = 17
bin_num = ""
bin_nums = []
for i in range(5):
    b = x % 2
    bin_nums.append(b)
    x = x // 2

    print(b)

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

results = []
for num1, num2 in zip(arr1, arr2):
    result_str = ""
    for i in range(5):
        rem1 = num1 % 2
        rem2 = num2 % 2

        ret = rem1 or rem2

        if ret:
            result_str += '#'
        else:
            result_str += ' '

        num1 = num1 // 2
        num2 = num2 // 2

    h = 'hello'

    tmp = ""
    for char in result_str[::-1]:
        tmp += char

    print(tmp)
    results.append(tmp)

# 실패율
from collections import Counter

N = 5
stages = [6, 6, 2, 6, 2, 4, 3, 1]
counter = Counter()

for stage in stages:
    counter[stage] += 1

x = len(stages)
fail_list = []
for i in range(N):
    # print(x, counter[i+1])
    fail_ratio = counter[i + 1] / x
    print(counter[i + 1], x)
    x -= counter[i + 1]
    fail_list.append(fail_ratio)

index_list = []
for i in range(len(fail_list)):
    index_list.append(fail_list.index(max(fail_list)) + 1)
    fail_list[fail_list.index(max(fail_list))] = -1