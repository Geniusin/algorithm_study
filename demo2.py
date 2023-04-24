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
for i in range(len_msg):
    for j in range(i, len_msg - i):
        search_word = msg[0:i+1]
        if search_word in msg:
            result.append(search_word)
        else:
            dict_res[search_word] = count
            count += 1

flag = True
while flag:






def solution(msg):
    msg_dict = dict()

    answer = []
    return answer