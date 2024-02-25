alpa_index = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}

def solution(msg):
    dict_idx = 27
    cnt = 0
    answer = []
    while True:

        lenght = 1
        now = cnt
        x = []
        while True:
            word = msg[now:now + lenght]
            if word in alpa_index.keys():
                x.append(word)
                lenght += 1
                if now + lenght == len(msg)+1:
                    cnt += 1
                    break

            else:
                alpa_index[word] = dict_idx
                cnt += (len(word) - 1)
                dict_idx += 1
                break
        answer.append(alpa_index[x[-1]])
        if cnt == (len(msg)-1):
            print(word, x, cnt, len(msg))
            break
    return answer