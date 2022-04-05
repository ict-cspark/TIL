# 1249. [S/W 문제해결 응용] 4일차 - 보급로

'''
2차 세계 대전에서 연합군과 독일군의 전투가 점점 치열해지고 있다.
전투가 진행중인 지역은 대규모 폭격과 시가전 등으로 인해 도로 곳곳이 파손된 상태이다.
그림 1(a)에서와 같이 도로들은 전투로 인해 트럭이나 탱크와 같은 차량들이 지날 갈 수 없다.
전투에서 승리하기 위해서는 기갑사단과 보급부대가 신속하게 이동하기 위한 도로가 있어야 한다.
공병대는 출발지(S) 에서 도착지(G)까지 가기 위한 도로 복구 작업을 빠른 시간 내에 수행하려고 한다.
도로가 파여진 깊이에 비례해서 복구 시간은 증가한다.
출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하시오.
깊이가 1이라면 복구에 드는 시간이 1이라고 가정한다.
'''

import sys
sys.stdin = open("input.txt", "r")

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]              # 델타 이용 (상 우 하 좌)

def BFS(sr, sc):                                        # BFS 함수 (시작 좌표 인덱스 값)
    queue = [(0, 0)]                                    # 큐에 시작 좌표 초기값으로 대입
    visited[sr][sc] = arr[sr][sc]                       # visited 리스트 시작위치에 arr[sr][sc] 값으로 초기화

    while queue:                                        # 큐가 비어있지 않을 때가지 반복문 실행
        r, c = queue.pop(0)                             # 앞에서 부터 큐를 하여 r, c에 저장

        for dr, dc in delta:                            # 델타 길이만큼 반복문 실행
            nr = r + dr                                 # nr에 r + dr 대입
            nc = c + dc                                 # nc에 c + dc 대입
            # 만약 nr과 nc가 인덱스 범위내이고 visited[nr][nc]의 값이 visited[r][c] + arr[nr][nc] 보다 작다면
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] > (visited[r][c] + arr[nr][nc]):
                queue.append((nr, nc))                  # 큐에 nr, nc 값 추가
                visited[nr][nc] = visited[r][c] + arr[nr][nc]   # visited[r][c] + arr[nr][nc] 값으로 갱신

    return visited[N - 1][N - 1]                        # 도착 좌표에 vistied 값 리턴

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                                    # 지도의 크기 N 입력받기
    arr = [list(map(int, input())) for _ in range(N)]   # 지도 정보 입력받아 arr에 저장
    visited = [[10000] * N for _ in range(N)]           # visited 리스트 생성하여 10000으로 초기화
    result = BFS(0, 0)                                  # BFS 함수 호출하고 리턴값 result에 저장

    print(f'#{test_case} {result}')                     # 결과값 출력