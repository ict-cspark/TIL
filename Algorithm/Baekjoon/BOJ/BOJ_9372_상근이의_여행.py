# Baekjoon Online Judge - 상근이의 여행

'''
상근이는 겨울방학을 맞아 N개국을 여행하면서 자아를 찾기로 마음먹었다.
하지만 상근이는 새로운 비행기를 무서워하기 때문에, 최대한 적은 종류의 비행기를 타고 국가들을 이동하려고 한다.
이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.
상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다.
'''


import sys
input = sys.stdin.readline

T = int(input())                        # 테스트 케이스 입력받기

for _ in range(T):                      # 테스트 케이스 만큼 반복
    N, M = map(int, input().split())    # 국가의 수와 비행기의 종류 입력받기

    nations = [[]for _ in range(N+1)]   # 국가 인접 리스트 생성

    for _ in range(M):                  # 비행 스케쥴 만큼 반복문 실행
        start, end = map(int, input().split()) # 비행 경로 입력 받기
        nations[start].append(end)      # 인접 리스트에 저장
        nations[end].append(start)

    visited = [0] * (N+1)               # 방문리스트 생성
    visited[1] = 1                      # 1번부터 방문 실행

    queue = [1]                         # queue에 1 추가
    result = 0                          # 결과값 출력을 위한 result 변수 생성
    while queue:                        # queue가 빌 때까지 반복문 실행
        idx = queue.pop(0)              # queue의 첫번째 요소 꺼내 idx에 저장
        while nations[idx]:             # nations[idx]가 비어있을 때까지 반복문 실행
            idx_n = nations[idx].pop(0) # nations[idx]의 첫번째 요소 꺼내와 idx_n에 저장
            if not visited[idx_n]:      # visited[idx_n]이 비어있지 않을 경우
                result += 1             # result에 1을 더함
                visited[idx_n] = 1      # 방문기록 남기기  
                queue.append(idx_n)     # queue에 idx_n 추가

    print(result)                       # 결과값 출력
