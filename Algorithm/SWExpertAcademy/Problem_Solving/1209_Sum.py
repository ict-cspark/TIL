# 1209. [S/W 문제해결 기본] 2일차 - Sum

'''
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
'''

import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 값 받기
T = 10

# 100x100 행렬 받아 이차원 행렬로 만들기
for t in range(1, T+1):
    t = int(input())
    arr = [list(map(int, input().split())) for n in range(100)]

    # 행, 열, 대각선, 역대각선 최댓값 저장을 위한 변수 선언
    r_max = 0
    c_max = 0
    diag = 0
    diag_reverse = 0
    for r in range(100):
        # 최댓값과 값 비교를 위한 초기값이 0인 변수 선언
        r_compare = 0
        c_compare = 0

        # 대각선의 합 저장
        diag += arr[r][r]
        diag_reverse += arr[r][99-r]

        # 한 행의 합과 한 행의 열의 합을 저장
        for c in range(100):
            r_compare += arr[r][c]
            c_compare += arr[c][r]

        # 행의 합 중 최대값 저장
        if r_compare > r_max:
            r_max = r_compare

        # 열의 합 중 최대값 저장
        if c_compare > c_max:
            c_max = c_compare

    # 이중 최대값만을 찾아서 출력
    max_result = c_max
    max_compare = 0
    if r_max > diag:
        if r_max > diag_reverse:
            max_compare = r_max
        else:
            max_compare = diag_reverse
    else:
        if diag > diag_reverse:
            max_compare = diag
        else:
            max_compare = diag_reverse

    if max_result > max_compare:
        print(f'#{t} {max_result}')
    else:
        print(f'#{t} {max_compare}')











