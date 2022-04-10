# Baekjoon Online Judge - 인구 이동

'''
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.
'''


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]                      # 델타리스트 생성
        
N, L, R = map(int, input().split())                             # 리스트 크기 N과 범위 L, R 입력 받기
ground = [list(map(int, input().split())) for _ in range(N)]    # 나라 인구 정보 입력받아 ground에 저장
    

day = 0                                                         # 날짜 정보 저장을 위해 day 변수 생성 후 초기화
while True:                                                     # break 만날 때까지 반복문 실행

    visited = [[0] * N for _ in range(N)]                       # 방문 흔적을 남기기 위한 visited 리스트 생성
    flag = 0                                                    # 국경 이동이 불가능한지 확인하기 위한 flag 변수 생성
    save = []                                                   # 1일차마다 인구정보 갱신을 위해 save 리스트 생성
    for sr in range(N):                                         # ground 크기만큼 반복문 실행
        for sc in range(N):

            if visited[sr][sc] == 1:                            # 만약 visited[sr][sc]가 방문한적 있으면 다음 반복문 실행
                continue
            queue = [(sr, sc)]                                  # 큐 생성하고 초기값으로 시작 좌표 대입
            visited[sr][sc] = 1                                 # 방문리스트에 방문흔적 남기기
            value = ground[sr][sc]                              # value 값에 출발위치의 인구정보 저장
            position = [(sr, sc)]                               # 국경을 허물 나라 위치를 담기위한 position 리스트 생성
            while queue:                                        # 큐가 빌때까지 반복문 실행
                r, c = queue.pop(0)                             # 큐의 첫번째 요소 꺼내와 r, c에 저장
                for dr, dc in delta:                            # 델타 크기만큼 반복문 실행
                    nr = dr + r                                 # nr, nc 생성하여 델타 위치 반영한 값 저장
                    nc = dc + c
                    # 만약 nr, nc가 인덱스 범위내이고 방문한적이 없다면
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                        ans = abs(ground[r][c] - ground[nr][nc])    # 출발 위치와 델타 이동한 위치의 인구 차이를 ans에 저장
                        if L <= ans <= R:                       # ans가 L, R 범위 내라면
                            queue.append((nr, nc))              # 큐에 현재 위치 좌표 추가하고
                            visited[nr][nc] = 1                 # 방문흔적 남기고
                            position.append([nr, nc])           # 포지션 리스트에 위치 추가하고
                            value += ground[nr][nc]             # value에 인구정보 저장

            if len(position) == 1:                              # 큐리스트가 비어서 반복문 종료했는데도 포지션 길이가 그대로 1이라면
                flag += 1                                       # flag에 1 더하고 다음 반복문 실행
                continue
            else:
                answer = value // len(position)                 # 포지션의 길이가 1이 아니라면 value를 포지션 길이로 나는 몫을 answer에 저장
                for pr, pc in position:                         # 포지션의 길이만큼 반복문 실행하여
                    save.append((pr, pc, answer))               # save 리스트에 answer 정보 추가해서 저장

    if flag == (N * N):                                         # 만약 ground 리스트 모두 탐색했는데 flag의 크기가 N*N 이라면
        print(day)                                              # day 출력하고 모든 반복문 종료
        break
    else:                                                       # 아닐경우에는
        for sar, sac, saa in save:                              # save 리스트를 불러와
            ground[sar][sac] = saa                              # ground 정보 갱신 후 
        day += 1                                                # day에 1을 더함