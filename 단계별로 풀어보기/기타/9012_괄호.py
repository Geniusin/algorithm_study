import sys
input = sys.stdin.readline

N = int(input())

list_par = []
for n in range(N):
    list_par.append(input()[:-1])

trg = '()'
for x in list_par:
    while True:
        if trg in x:
            x = x.replace("()", "")
        else:
            break

    if x == "":
        print('YES')
    else:
        print('NO')

