import sys
from collections import deque                                   # 시간 초과를 해결하기 위해 deque 사용

sys.stdin = open("input.txt", "r")


def BFS(N, M, C):                                               # BFS 함수 사용 (자연수 N, M, 횟수 C)
    queue = deque([(N, C)])                                     # deque를 생성하고 N, C를 대입
    number = set()                                              # 중복 값을 피하기 위해 set으로 number 생성
    number.add(N)                                               # 초기값 N 대입

    while queue:                                                # 큐가 비어있지 않을때까지 반복
        N, C = queue.popleft()                                  # deque에서 앞에서 popleft 하여 N, C에 각각 저장

        if N == M:                                              # N과 M이 같다면 C를 리턴
            return C
        if N + 1 not in number and 0 < N + 1 <= 1000000:        # N + 1의 값이 number에 없고 범위 내일 경우
            queue.append((N + 1, C + 1))                        # N + 1 값과 C에 1을 더하여 큐에 추가
            number.add(N + 1)                                   # number 집합에 N + 1 값 추가
        if N - 1 not in number and 0 < N - 1 <= 1000000:        # N - 1의 값이 number에 없고 범위 내일 경우
            queue.append((N - 1, C + 1))                        # N - 1 값과 C에 1을 더하여 큐에 추가
            number.add(N - 1)                                   # number 집합에 N - 1 값 추가
        if N * 2 not in number and 0 < N * 2 <= 1000000:        # N * 2의 값이 number에 없고 범위 내일 경우
            queue.append((N * 2, C + 1))                        # N * 2 값과 C에 1을 더하여 큐에 추가
            number.add(N * 2)                                   # number 집합에 N * 2 값 추가
        if N - 10 not in number and 0 < N - 10 <= 1000000:      # N - 10의 값이 number에 없고 범위 내일 경우
            queue.append((N - 10, C + 1))                       # N - 10 값과 C에 1을 더하여 큐에 추가
            number.add(N - 10)                                  # number 집합에 N - 10 값 추가


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())                            # 두 자연수 N, M 입력받기

    result = BFS(N, M, 0)                                       # BFS 함수 호출하고 리턴값 result에 저장
    print(f'#{test_case} {result}')                             # 결과 값 호출