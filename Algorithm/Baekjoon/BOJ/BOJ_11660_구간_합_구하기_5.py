# Baekjoon Online Judge - 구간 합 구하기 5

'''
표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())                                # 표의 크기와 횟수 M 입력받기
table = [list(map(int, input().split())) for _ in range(N)]     # N 줄 입력받아 table에 저장

table = [[0] * N] + table                                       # table에 0으로 채운 리스트 맨 앞에 추가
for r in range(1, N + 1):                                       # 1부터 N까지 반복문 실행
    for c in range(N):                                          # 열 길이만큼 반복문 실행하여
        table[r][c] += table[r-1][c]                            # table[r][c] 값에 이전행의 값 누적하기

for _ in range(M):                                              # 시행횟수만큼 반복문 실행
    answer = 0                                                  # 결과값 저장을 위한 answer 변수 실행
    sr, sc, er, ec = map(int, input().split())                  # 좌표값 입력받기
    for i in range(sc - 1, ec):                                 # 열 범위만큼 반복문 실행
        answer += (table[er][i] - table[sr - 1][i])             # answer에 마지막 행의 값에서 시작행 전의 행의값의 차이를 더함
    print(answer)                                               # 결과값 출력