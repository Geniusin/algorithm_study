import math
import re


def solution(str1, str2):
    ans = 1
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1) - 1):
        word = str1[i:i + 2]
        p = re.search('[a-z]+', word)
        if p != None:
            if len(p.group(0)) == 2:
                str1_list.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        word = str2[i:i + 2]
        p = re.search('[a-z]+', word)
        if p != None:
            if len(p.group(0)) == 2:
                str2_list.append(str2[i:i + 2])

    if len(str1_list) == 0 and (str2_list) == 0:
        ans = 65536
        return ans


    else:
        all_set = set(str1_list) | set(str2_list)
        dict_1 = dict()
        for str1 in str1_list:
            if str1 not in dict_1:
                dict_1[str1] = 1
            else:
                dict_1[str1] += 1

        dict_2 = dict()
        for str2 in str2_list:
            if str2 not in dict_2:
                dict_2[str2] = 1
            else:
                dict_2[str2] += 1

        cnt_gyo = 0
        cnt_hab = 0
        for word in all_set:

            if (word in dict_1) & (word in dict_2):
                cnt_gyo += min(dict_1[word], dict_2[word])
                cnt_hab += max(dict_1[word], dict_2[word])

            elif (word in dict_1) & (word not in dict_2):
                cnt_hab += dict_1[word]

            elif (word not in dict_1) & (word in dict_2):
                cnt_hab += dict_2[word]

        if (cnt_gyo == 0) and (cnt_hab != 0):
            ans = 0
        elif (cnt_gyo != 0) and (cnt_hab == 0):
            ans = 65536
        elif (cnt_gyo == 0) and (cnt_hab == 0):
            ans = 65536
        else:
            ans = math.trunc((cnt_gyo / cnt_hab) * 65536)

        return ans