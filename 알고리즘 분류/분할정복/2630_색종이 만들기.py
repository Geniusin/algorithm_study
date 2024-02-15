b = 0
w = 0
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def make(start, end, lenght):
    global b, w
    if lenght < 1: return
    half = lenght // 2
    for y in range(start, start+lenght):
        for x in range(end, end+lenght):
            if paper[start][end] != paper[y][x]:

                make(start, end, half)
                make(start, end+half, half)
                make(start + half, end, half)
                make(start + half, end + half, half)
                return

    if paper[start][end] == 1:
        b += 1
    elif paper[start][end] == 0:
        w += 1

make(0, 0, N)
print(w)
print(b)