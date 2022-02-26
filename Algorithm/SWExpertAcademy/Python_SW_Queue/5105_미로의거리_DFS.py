import sys
sys.stdin = open("input.txt", "r")

def startFind(arr, N):              # 출발점을 찾는 함수
    for r in range(N):              # 배열의 크기만큼 반복문 실행
        for c in range(N):
            if arr[r][c] == 2:      # 현재 원소가 2일 경우
                return r, c         # r과 c를 리턴
    return -1, -1                   # 출발지를 찾지 못했을 경우 -1, -1을 리턴

def dfs(r, c, N, move):             # DFS 알고리즘을 이용하여 도착지를 찾는 함수 (move는 지나온 칸수)
    global minV                     # minV 변수를 이용하기 위해 global 사용
    if maze[r][c] == 3:             # 도착점을 찾았을 경우 이동한 값이 min값보다 작다면 값을 변경
        if minV > move:
            minV = move

    else:
        maze[r][c] = 1              # 아닐경우 무한루프 방지를 위해 maze 위치를 1로 변경
        dr = [0, 1, 0, -1]          # 상, 우, 하, 좌
        dc = [-1, 0, 1, 0]
        for d in range(4):          # 델타를 이용하기 위해 반복문 실행
            nr = r + dr[d]          # nr, nc값을 생성하여 델타 값만큼 변경
            nc = c + dc[d]
            # 만약 nr과 nc가 인덱스 범위 안이고 maze[nr][nc]가 1이 아닐경우
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1:
                dfs(nr, nc, N, move + 1)        # 새로운 좌표 값 nr, nc와 move에 1을 더한 값을 호출
        maze[r][c] = 0              # 반복문을 빠져나올 경우 최솟값을 위한 또다른경로를 찾기 위해 현재위치를 0으로 변경 후 리턴
    return

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sR, sC = startFind(maze, N)             # 입력받은 배열에서 2를 찾아 시작점의 좌표를 저장
    minV = N * N

    dfs(sR, sC, N, 0)                       # 출발점에서 도착점까지 최소의 경로를 찾아 반환

    if minV == N * N:                       # 만약 minV 값이 변경되지 않았다면 도착지를 못찾았으므로 값을 0을 출력하기 위해 1로 변경
        minV = 1
    print(f'#{test_case} {minV - 1}')       # 이동한 칸수만 출력하기 위해 min 값에서 1을 뺀 결과값을 출력