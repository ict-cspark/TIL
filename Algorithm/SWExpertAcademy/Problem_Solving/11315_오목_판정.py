# 11315. 오목 판정

'''
N X N 크기의 판이 있다.
판의 각 칸에는 돌이 있거나 없을 수 있다. 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.
교착 상태의 개수를 구하라.
'''

import sys
sys.stdin = open("input.txt", "r")

def check(go, N):
    dr = [0, 1, 1, 1] # 오른쪽, 아래, 왼쪽 아래 대각선, 오른쪽 아래 대각선
    dc = [1, 0, -1, 1]

    for r in range(N):
        for c in range(N):
            if go[r][c] == 'o':
                for d in range(4):
                    count = 0
                    nr = r
                    nc = c
                    for _ in range(5):
                        if 0 <= nr < N and 0 <= nc < N and go[nr][nc] == 'o':
                            count += 1
                            nr += dr[d]
                            nc += dc[d]

                    if count == 5:
                        return 'YES'
    return 'NO'

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    go = [input() for _ in range(N)]
    result = check(go, N)

    print(f'#{test_case} {result}')