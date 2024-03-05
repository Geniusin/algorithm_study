import sys
input = sys.stdin.readline


boards = input()[:-1].split('.')

poly_A = 'AAAA'
poly_B = 'BB'

xs = []
result = 1
for board in boards:
    x = ''
    if len(board) % 2 != 0:
        result = -1
        break

    else:
        cnt_A = len(board) // 4
        cnt_B = (len(board) % 4) // 2

        if (len(board) % 4) % 2 != 0:
            result = -1
            break
        else:
            x = x + poly_A*cnt_A + poly_B*cnt_B

    xs.append(x)

if result == -1:
    print(-1)
else:
    print('.'.join(xs))