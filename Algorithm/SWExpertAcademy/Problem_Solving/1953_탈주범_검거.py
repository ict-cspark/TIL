# 1953. [모의 SW 역량테스트] 탈주범 검거

'''
지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때 탈주범이 위치할 수 있는 장소의 개수를 계산하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")

# pipe 방향 정보와 도착지 파이프와 일치하는 방향 정보 arrive와 델타 리스트 delta 생성
pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
arrive = [1, 0, 3, 2]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(r, c, l):                                           # BFS를 수행하는 함수
    result = 1                                              # 이동가능한 파이프 갯수를 구하기 위한 변수로 초기값 1로 설정
    queue = [(r, c)]                                        # 큐에 초기값으로 맨홀 위치 저장
    visit[r][c] = 1                                         # visit 리스트의 맨홀 위치에 1 대입

    while queue:                                            # 큐가 비어있지 않을때까지 반복문 실행
        r, c = queue.pop(0)

        if visit[r][c] == l:                                # visit[r][c]의 값이 탈출 시간과 일치하면 result 값을 반환
            return result
        for i in range(4):                                  # 델타 길이만큼 반복문 실행
            nr = r + delta[i][0]                            # r에 델타 위치를 더한 nr을 생성
            nc = c + delta[i][1]                            # c에 델타 위치를 더한 nc를 생성
            # 만약 nr과 nc가 인덱스 범위내에 있고 출발 할 파이프의 델타 방향이 있으면서, 도착 할 파이프의 델타 상호 방향도 있으면서 방문한 적이 없을 경우에  
            if 0 <= nr < N and 0 <= nc < M and pipe[t_map[r][c]][i] and pipe[t_map[nr][nc]][arrive[i]] and visit[nr][nc] == 0:
                queue.append((nr, nc))                      # 큐에 도착하는 파이프의 값을 추가하고
                visit[nr][nc] = visit[r][c] + 1             # 출발한 파이프의 visit 값에 1을 더한 값을 visit에 저장
                result += 1                                 # 이동한 파이프 갯수에 1을 더함

    return result                                           # 탈출 시간전에 큐가 비어질 경우 더이상 실행하지 않고 result 값을 리턴

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())               # 세로 크기 N, 가로 크기 M, 맨홀 세로 위치 R, 멘홀 가로 위치 C, 탈출 시간 L    
    t_map = [list(map(int, input().split())) for _ in range(N)] # 터널 지도를 t_map 리스트에 저장
    visit = [[0] * M for _ in range(N)]                     # 0으로 채운 방문 확인용 visit 리스트 생성

    result = BFS(R, C, L)                                   # BFS 함수를 호출하여 인자 값으로 R, C, L 대입

    print(f'#{test_case} {result}')                         # 결과값 출력