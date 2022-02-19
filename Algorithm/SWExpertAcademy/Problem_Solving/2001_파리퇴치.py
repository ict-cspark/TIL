# 2001. 파리 퇴치

'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    # 배열 길이 N과 파리채 길이 M 입력 받기
    N, M = map(int, input().split())
    # MxM 2차원 행렬 만들어서 입력 받기
    arr = []
    for n in range(N):
        arr += [list(map(int, input().split()))]

    max_arr = 0
    for r in range((N - M) + 1):
        for c in range((N - M) + 1):
            bugs = 0
            for rm in range(M):
                for cm in range(M):
                    bugs += arr[r + rm][c + cm]
            if max_arr < bugs:
                max_arr = bugs

    print(f'#{test_case} {max_arr}')
