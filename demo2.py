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

flag = True
while flag:






def solution(msg):
    msg_dict = dict()

    answer = []
    return answer