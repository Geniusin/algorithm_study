w2n = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def solution(s):
    while True:
        flag = False
        for word in list(w2n.keys()):
            if word in s:
                lenght = len(word)
                start = s.index(word)
                s = s.replace(s[start: start + lenght], str(w2n[word]))
                print(s)
                flag = True

                break
        if not flag:
            break
    answer = int(s)

    return answer