x_in = [[1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1]]

def d_c(arr, lenght):

    tmp_sum = 0
    for ar in arr:
        tmp_sum += sum(ar)

    start = 0
    half = int(lenght/2)
    tmp1 = []
    for i in x_in[start:half]:
        tmp1.append(i[start:half])

    if (tmp_sum == lenght**2) or (tmp_sum == 0):
        return 1
    else:

        half = int(lenght/2)
        tmp1 = []
        for i in x_in[:half]:
            tmp1.append(i[:half])
        return d_c(tmp1, half)

        tmp2 = []
        for i in x_in[half:lenght]:
            tmp2.append(i[half:lenght])
        return d_c(tmp2, half)

        tmp3 = []
        for i in x_in[:half]:
            tmp3.append(i[half:lenght])
        return d_c(tmp3, half)

        tmp4 = []
        for i in x_in[half:lenght]:
            tmp4.append(i[:half])
        return d_c(tmp4, half)

x = d_c(x_in, len(x_in))

tmp = []
for i in x_in[:4]:
    tmp.append(i[:4])