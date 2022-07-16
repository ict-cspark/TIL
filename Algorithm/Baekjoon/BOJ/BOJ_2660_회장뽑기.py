# Baekjoon Online Judge - 회장뽑기

import sys
input = sys.stdin.readline

'''
회장은 회원들 중에서 점수가 가장 작은 사람이 된다. 
회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오.
'''

INF = int(1e9)                  # 임의의 큰 값 INF로 설정

N = int(input())                # 회원의 수 N 입력 받기

graph = [[INF] * (N + 1) for _ in range(N + 1)]     # N + 1 * N + 1 크기으 2차원 리스트 만들어 INF 초기값으로 설정

for a in range(1, N + 1):       # 1 부터 N + 1 까지 반복문 실행
    for b in range(1, N + 1):
        if a == b:              # a와 b가 같을 경우 graph에 0으로 채움
            graph[a][b] = 0

while True:                     # while 반복문 실행
    a, b = map(int, input().split())    # a, b로 입력 받기
    if a == -1 and b == -1:     # a와 b가 -1일 경우 반복문 종료
        break
    else:
        graph[a][b] = 1         # 아닐 경우 graph에 1을 채움
        graph[b][a] = 1

for k in range(1, N + 1):       # 플로이드 와샬 알고리즘 적용하기 위해 모두 탐색하기위해 k번 반복
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = [[] for _ in range(N + 1)]     # result 2차원 빈 리스트 생성
for i in range(1, N + 1):
    idx_max = max(graph[i][1:])         # graph[i]의 가장 큰값을 idx_max에 저장
    result[idx_max].append(i)           # result[idx_max]에 i값을 추가

for j in range(1, N + 1):
    if result[j]:                       # result[j]가 비어있지 않을 경우
        print(j, len(result[j]))        # 회장 점수와 회장 인원 출력
        print(*result[j])               # result[j] 출력
        break                           # 반복문 종료
