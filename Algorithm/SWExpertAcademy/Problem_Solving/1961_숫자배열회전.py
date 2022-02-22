# 1961. 숫자 배열 회전

'''
N x N 행렬이 주어질 때,

시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    result = 0
    # 리스트 크기를 나타내는 N 입력받기
    N = int(input())
    # N줄만큼 입력받아 2차원 리스트로 저장
    num = []
    for _ in range(N):
        num += [list(map(int, input().split()))]

    # 90도 180도 270도 빈 리스트 각각 만들기
    num_90 = [[0] * N for _ in range(N)]
    num_180 = [[0] * N for _ in range(N)]
    num_270 = [[0] * N for _ in range(N)]

    # N만큼 행과 열을 반복하여 각각 리스트에 저장
    # 90도, 180, 270도로 변할 때 공통된 규칙 찾기
    for r in range(N):
        for c in range(N):
            num_90[r][c] = num[N - c -1][r]
            num_180[r][c] = num[N - r - 1][N - c -1]
            num_270[r][c] = num[c][N - r - 1]

    # 결과값 join을 이용하여 출력
    print(f'#{test_case}')
    for i in range(N):
        print("".join(map(str, num_90[i])),end=" ")
        print("".join(map(str, num_180[i])),end=" ")
        print("".join(map(str, num_270[i])))