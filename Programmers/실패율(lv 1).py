def solution(N, stages):
    answer = []
    res = []
    fail_rat = 0
    for n in range(1, N + 1):
        reached = sum([1 for s in stages if s >= n])
        not_clear = sum([1 for s in stages if s == n])

        if reached == 0:
            fail_rat = 0
        else:
            fail_rat = not_clear / reached
        res.append(fail_rat)

    res_rev = sorted(res, reverse=True)

    for i in range(len(res)):
        rank = res.index(res_rev[i])

        answer.append(res.index(res_rev[i]) + 1)
        res[rank] = -1
    return answer