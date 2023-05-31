x_in = [[1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1]]

b = 0
w = 0
def make(start, end, lenght):
    global b, w
    print(x_in[start][end])
    # if lenght < 1: return
    half = lenght // 2
    for y in range(start, start + half):
        for x in range(end, end + half):
            if x_in[start][end] != x_in[y][x]:

                make(start, end, half)
                make(start, end+half, half)
                make(start + half, end, half)
                make(start + half, end + half, half)
                return

    if x_in[start][end] == 1:
        b += 1
    elif x_in[start][end] == 0:
        w += 1

make(0, 0, 8)
print(b, w)