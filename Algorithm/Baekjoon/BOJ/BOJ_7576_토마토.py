# Baekjoon Online Judge - 토마토

'''
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 델타를 위한 리스트 생성 ( 상, 우, 하, 좌 )
queue = deque()                             # deque 생성

for i in range(N):                          # 2차원 배열에서 토마토가 있는 1을 찾아 queue에 저장
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j, 1])
day = 1
while queue:                                # 큐가 비어있지 않을 경우 계속 반복문 실행
    r, c, day = queue.popleft()             # popleft를 하여 앞쪽부터 꺼내와 좌표와 day 저장
    for dr, dc in delta:                    # 델타 4방향 만큼 반복
        nr = r + dr                         # 새로운 좌표 nr, nc 저장
        nc = c + dc
        # 만약 nr과 nc가 인덱스 범위 내에 있고 해당 좌표가 0일 경우
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            queue.append([nr, nc, day + 1]) # 큐에 해당 좌표와 day에 + 1 값을 저장
            arr[nr][nc] = day + 1           # 해당 좌표에 day + 1 값으로 바꿈

result = 0
for n in range(N):                          # 행 길이 만큼 반복문 실행
    if 0 in arr[n]:                         # 해당 행에 0 이 있을 경우 result에 0을 저장하고 반복문 종료
        result = 0
        break
    elif result < max(arr[n]):              # 아닐 경우 해당 행에 최댓값이 result보다 크다면 값 교체
        result = max(arr[n])

print(result - 1)                           # 첫째날은 0일차이므로 결과값에서 -1을 출력