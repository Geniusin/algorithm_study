import sys
input = sys.stdin.readline

arr_b = ['BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB']

arr_w = ['WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW']
M, N = map(int, input().split())

ches_board =[input().split() for _ in range(M)]

result = 99999999999
c_start = 0
c_end = 8

while c_end < M+1:

    r_start = 0
    r_end = 8
    while r_end < N+1:

        tmp = ches_board[c_start:c_end]
        for i, j in enumerate(tmp):
            tmp[i] = j[0][r_start:r_end]

        tmp_res_1 = 0
        tmp_res_2 = 0

        for board, arr in zip(tmp, arr_b):
            for b_char, arr_char in zip(board, arr):

                if b_char != arr_char:
                    tmp_res_1 += 1


        for board, arr in zip(tmp, arr_w):
            for b_char, arr_char in zip(board, arr):

                if b_char != arr_char:
                    tmp_res_2 += 1


        r_start += 1
        r_end += 1

        result = min(result, tmp_res_1, tmp_res_2)
        if result == 0: break

    if result == 0: break

    c_start += 1
    c_end += 1

print(result)