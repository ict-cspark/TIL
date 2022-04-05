import sys
sys.stdin = open("input.txt", "r")

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]                      # 델타를 이용하기 위한 리스트 생성 (상, 우, 하, 좌)


def BFS(sr, sc):                                                # BFS 함수 실행
    queue = [(sr, sc)]                                          # 큐 생성하고 초깃값으로 sr, sc값 대입
    fuel = [[10000] * N for _ in range(N)]                      # 연료 소비량 표시하기 위한 fuel 리스트 생성
    fuel[sr][sc] = 0                                            # fuel[sr][sc]위치에 0 대입

    while queue:                                                # 큐가 비어있지 않을때까지 반복문 실행
        r, c = queue.pop(0)                                     # 앞에서 부터 팝하여 r,c에 저장
        for dr, dc in delta:                                    # 델타 길이만큼 반복문 실행
            nr = r + dr                                         # nr에 r + dr 값 대입
            nc = c + dc                                         # nc에 c + dc 값 대입
            if 0 <= nr < N and 0 <= nc < N:                     # nr과 nc가 인덱스 범위 내에 있으면 조건문 실행
                value = fuel[r][c] + 1                          # value에 fuel[r][c] + 1 값 저장
                height = arr[nr][nc] - arr[r][c]                # arr[nr][nc] - arr[r][c] 차이를 distance에 저장
                if height > 0:                                  # 높이차이가 1보다 크다면
                    value += height                             # value에 높이 더하기
                if fuel[nr][nc] > value:                        # fuel[nr][nc]값보다 value가 작다면
                    queue.append((nr, nc))                      # 큐에 현재 좌표 위치 추가하고
                    fuel[nr][nc] = value                        # value값으로 갱신

    return fuel[N - 1][N - 1]                                   # fuel[N - 1][N - 1] 우측 하단값 리턴


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                                            # 지역 크기 N 입력 받기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 지역 정보 입력받아 arr에 저장 

    result = BFS(0, 0)                                          # BFS 함수 실행하여 result에 저장
    print(f'#{test_case} {result}')                             # 결과값 출력