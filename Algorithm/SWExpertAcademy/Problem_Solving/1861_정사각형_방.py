# 1861. 정사각형 방

'''
N2개의 방이 N×N형태로 늘어서 있다.
위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")                          

# 테스트케이스 입력받기
T = int(input())

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]                  # 델타 이동을 위한 델타 리스트 생성

def BFS(sr, sc):                                            # BFS 를 위한 함수 생성
    queue = [(sr, sc)]                                      # 큐에 초기값으로 시작값을 대입
    move = [room[sr][sc]]                                   # 이동한 길이와 값을 저장하기 위한 move 리스트 생성 후 초기값으로 시작값 대입
    visit[sr][sc] = 1                                       # 방문 리스트에 해당 인덱스 위치에 1을 대입

    while queue:                                            # 큐가 비어있지 않을 경우 반복문 계속 실행
        r, c = queue.pop(0)                                 # 큐에 첫번째 원소를 꺼내와 r, c에 저장
        for dr, dc in delta:                                # 델타 방향만큼 반복문 실행
            nr = r + dr                                     # r + dr 의 값을 nr에 저장
            nc = c + dc                                     # c + dc 의 값을 nc에 저장
            # 만약 nr과 nc가 인덱스 범위 내이고 room[r][c]와 room[nr][nc]의 절댓값 차가 1일 경우
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0 and abs(room[r][c] - room[nr][nc]) == 1:
                queue.append((nr, nc))                      # 큐에 이동한 위치의 값을 추가하고
                visit[nr][nc] = 1                           # 방문 리스트에 1을 대입
                move.append(room[nr][nc])                   # move 리스트에 현재 값을 추가

    return min(move), len(move)                             # move리스트의 최솟값과 move리스트의 길이를 리턴


for test_case in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]  # 방 정보를 room 리스트에 저장
    visit = [[0] * N for _ in range(N)]                     # 방문 기록을 남기기 위한 visit리스트 생성

    num = N * N                                             # 최솟값을 찾기 위한 num 변수 생성후 초깃값으로 N*N 값 저장
    count = 0                                               # 연속 된 숫자 갯수를 저장하기 위한 count 변수 생성 후 초깃값으로 0을 저장
    for sr in range(N):                                     # room 배열 크기만큼 행, 열 반복문 실행
        for sc in range(N):     
            f, n = BFS(sr, sc)                              # sr과 sc 값으로 BFS 함수를 호출하고 반환 값을 f와 n에 저장
            if count < n or (count == n and num > f):       # 만약 conut가 n보다 작거나 혹은 conut와 n이 같지만 num이 f보다 클 경우
                count = n                                   # count에 n을 대입
                num = f                                     # num에 f를 대입

    print(f'#{test_case} {num} {count}')                    # 결과값 출력