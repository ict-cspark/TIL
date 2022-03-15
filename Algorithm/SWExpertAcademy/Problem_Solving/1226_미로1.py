# 1226. [S/W 문제해결 기본] 7일차 - 미로1

'''
16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.
가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.
주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")

def MazeStart(arr):                     # 출발점을 찾는 함수
    for i in range(16):                 # 배열의 크기만큼 반복문 실행
        for j in range(16):
            if arr[i][j] == 2:          # 현재 원소가 2일 경우
                return i, j             # i와 j를 리턴
    return -1, -1                       # 출발지를 찾지 못했을 경우 -1, -1을 리턴

def BFS(r, c, arr):                     # 도착지를 BFS 알고리즘을 이용하여 찾는 함수
    visit = [[0] * 16 for _ in range(16)]           # 방문흔적을 남기기위한 미로와 동일한 크기의 배열 생성
    delta = [(-1, 0), (0, 1), (1, 0 ), (0, -1)]     # 델타를 위한 리스트 생성 (상, 우, 하, 좌)
    queue = [(r, c)]                                # 실시간 이동경로 저장을 위한 큐를 생성하고 초기값으로 출발지의 위치를 설정
    visit[r][c] = 1                                 # 방문리스트 초기값으로 출발지 위치에 1을 대입

    while queue:                                    # 큐가 비어있지 않을 때까지 반복문 실행
        r, c = queue.pop(0)                         # 큐의 첫번째 값을 튜플 형태로 꺼내와 r과 c에 각각 저장
        if arr[r][c] == 3:                          # 만약 arr[r][c]의 값이 3이라면
            return 1                                # 미로가 막히지 않았으므로 1을 리턴
        else:
            for dr, dc in delta:                    # 델타를 적용하기 위해 반복문 실행
                nr = r + dr                         # 현재 좌표값에 델타 거리만큼 적용하여 새로운 변수 생성
                nc = c + dc
                # 만약 nr과 nc가 인덱스 범위내에 존재하고 값이 1(벽)이 아니고 방문한적이 없다면 아래 조건문 실행
                if 0 < nr < 15 and 0 < nc < 15 and arr[nr][nc] != 1 and visit[nr][nc] == 0:
                    visit[nr][nc] = 1               # 방문흔적을 남기기위해 방문리스트에 1을 저장
                    queue.append((nr, nc))          # 큐에 해당 위치의 인덱스 값을 추가
    return 0    # 큐가 비어있을때까지 도착지를 찾지 못했으므로 해당 미로는 막혀있는 상태인 0을 리턴


# 테스트케이스 입력받기
T = 10

for _ in range(1, T + 1):
    test_case = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    sR, sC = MazeStart(arr)                         # 입력받은 배열에서 2를 찾아 시작점의 좌표를 저장
    result = BFS(sR, sC, arr)                       # 미로에서 도착지를 찾을 수있으면 1 아니면 0을 저장
    print(f'#{test_case} {result}')                 # 결과값을 출력