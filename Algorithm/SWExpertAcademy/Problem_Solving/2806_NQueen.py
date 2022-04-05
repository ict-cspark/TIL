# 2806. N-Queen

'''
N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open("input.txt", "r")


def check(sr, sc):                                  # check 함수
    for i in range(sr - 1, -1, -1):                 # 위의 방향으로 탐색하면서
        if visited[i][sc] == 1:                     # 말이 있으면
            return 0                                # False 리턴

    li = sr - 1                                     # 왼쪽 대각선 탐색
    lj = sc - 1
    while li >= 0 and lj >= 0:                      # 인덱스 범위 내이고
        if visited[li][lj] == 1:                    # 말이 있으면
            return 0                                # False 리턴
        li -= 1                                     # 한칸씩 이동
        lj -= 1

    ri = sr - 1                                     # 오른쪽 대각선 탐색
    rj = sc + 1
    while ri >= 0 and rj < N:                       # 인덱스 범위 내이고
        if visited[ri][rj] == 1:                    # 말이 있으면
            return 0                                # False 리턴
        ri -= 1                                     # 한칸씩 이동
        rj += 1

    return 1                                        # 모든 경우에 말이 없으면 만족하므로 True 리턴

def DFS(r):                                         # DFS 함수 실행
    global result                                   # global result 변수로 호출
    if r == N:                                      # r과 N이 같을 경우 모든 경우 만족하므로
        result += 1                                 # result에 1을 더하고 리턴
        return
    else:
        for c in range(N):                          # 열을 반복하면서
            if check(r, c):                         # check 함수 실행
                visited[r][c] = 1                   # 방문 흔적 1로 갱신
                DFS(r + 1)                          # DFS(r+1) 재호출
                visited[r][c] = 0                   # 방문 흔적 다시 지우기
    return


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                                # 보드의 크기 N 입력받기
    visited = [[0] * N for _ in range(N)]           # 방문 리스트 생성

    result = 0                                      # 결과 값 저장을 위한 변수 생성
    DFS(0)                                          # DFS 함수 호출
    print(f'#{test_case} {result}')                 # 결과값 출력