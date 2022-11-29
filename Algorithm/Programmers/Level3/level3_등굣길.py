# Programmers - Level3 - 등굣길

def solution(m, n, puddles):
    maps = list([0] * (m + 1) for _ in range(n + 1))
    maps[1][1] = 1

    for rn in range(1, n + 1):
        for cm in range(1, m + 1):
            if rn == cm == 1:
                continue
            if [cm, rn] in puddles:
                maps[rn][cm] = 0
            else:
                top = maps[rn - 1][cm]
                left = maps[rn][cm - 1]
                maps[rn][cm] = top + left

    answer = maps[n][m] % (1000000007)
    return answer