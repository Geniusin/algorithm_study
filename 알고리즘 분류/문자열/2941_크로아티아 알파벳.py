import sys
input = sys.stdin.readline

input_str = input()[:-1]


alpas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

alpas_cro2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
alpas_cro3 = ['dz=']




start_idx = 0
num_alpas = 0


while True:
    flag = False
    for cro3 in alpas_cro3:
        if input_str[start_idx: start_idx+3] == cro3:
            start_idx += 3
            num_alpas += 1
            flag = True
            break
    if flag:
        continue

    for cro2 in alpas_cro2:
        if input_str[start_idx: start_idx+2] == cro2:
            start_idx += 2
            num_alpas += 1
            flag = True
            break
    if flag:
        continue

    for alpa in alpas:
        if input_str[start_idx: start_idx+1] == alpa:
            start_idx += 1
            num_alpas += 1
            flag = True
            break
    if flag:
        continue

    if start_idx >= len(input_str):
        break

print(num_alpas)
