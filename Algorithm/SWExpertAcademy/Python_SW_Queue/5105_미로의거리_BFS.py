import sys
sys.stdin = open("input.txt", "r")

def startFind(arr, N):              # 출발점을 찾는 함수
    for r in range(N):              # 배열의 크기만큼 반복문 실행
        for c in range(N):
            if arr[r][c] == 2:      # 현재 원소가 2일 경우
                return r, c         # r과 c를 리턴
    return -1, -1                   # 출발지를 찾지 못했을 경우 -1, -1을 리턴

def bfs(r, c, arr, N):              # 도착지를 bfs 알고리즘을 이용하여 찾는 함수
    visited = [[0] * N for _ in range(N)]       # 방문흔적을 남기기위한 미로와 동일한 크기의 배열 생성
    queue = []                      # 실시간 이동경로 저장을 위한 큐 생성
    queue.append((r, c))            # 큐의 초기값으로 출발지의 위치를 설정
    visited[r][c] = 1               # 출발지 위치에 1을 설정
    while queue:                    # 큐가 비어있을 경우 while문 종료
        r, c = queue.pop(0)         # 큐의 첫번째 값을 튜플 형태로 꺼내와 r과 c에 각각 저장
        if arr[r][c] == 3:          # 만약 arr[r][c]의 값이 3이라면
            return visited[r][c] - 2    # 이동한 칸수만 반환하기 위해 -2 한 값을 리턴

        else:
            dr = [0, 1, 0, -1]      # 상, 우, 하, 좌
            dc = [-1, 0, 1, 0]
            for d in range(4):      # 델타를 적용하기 위해 반복문 실행
                nr = r + dr[d]      # 현재 좌표값에 델타 거리만큼 적용하여 새로운 변수 생성
                nc = c + dc[d]      
                # 만약 nr과 nc가 인덱스 범위내에 존재하고 값이 1(벽)이 아니고 방문한적이 없다면 아래 조건문 실행
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1         # 직전 방문한 곳에 visited 값에 +1을 하여 visited 값에 저장
                    queue.append((nr, nc))                      # 큐에 해당 인덱스 추가

    return 0            # while문을 빠져나올 경우 도착지를 못찾은 경우이므로 0을 리턴


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sR, sC = startFind(maze, N)                 # 입력받은 배열에서 2를 찾아 시작점의 좌표를 저장
    result = bfs(sR, sC, maze, N)               # 출발점에서 도착점까지 최소의 경로를 찾아 반환

    print(f'#{test_case} {result}')             # 결과값 출력