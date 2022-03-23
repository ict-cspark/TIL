import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())                    # 노드 V와 간선 E의 정보를 입력 받기
    graph = [[0] * (V + 1) for _ in range(V + 1)]       # 그래프 정보를 담기 위한 리스트 생성

    for _ in range(E):                                  # 간선 갯수만큼 반복문 실행
        X, Y = map(int, input().split())                # X, Y로 입력받기
        graph[X][Y] = 1                                 # graph[X][Y]에 1 대입
        graph[Y][X] = 1                                 # graph[Y][X]에 1 대입
    S, G = map(int, input().split())                    # 출발노드 S와 도착노드 G 입력 받기

    visit = [0] * (V + 1)                               # 방문기록을 남기기 위한 visit 리스트 생성
    visit[S] = 1                                        # visit[S] 에 1을 대입하여 초기값 설정
    queue = [S]                                         # 큐에 출발 노드 저장
    result = 0                                          # 결과값 저장을 위한 result 변수 생성
    while queue:                                        # 큐가 비어있을 때까지 반복문 실행
        r = queue.pop(0)                                # r에 큐 리스트에 첫번째 값 pop
        if r == G:                                      # r이 G와 같을 경우
            result = visit[r] - 1                       # result에 visit[r] - 1 값 저장 후 break
            break
        for c in range(V + 1):                          # V + 1만큼 반복문 실행
            if graph[r][c] == 1 and visit[c] == 0:      # 만약 graph[r][c] 값이 1이고 visit[c]의 값이 0일 경우
                queue.append(c)                         # 큐에 c값 추가
                visit[c] = visit[r] + 1                 # visit[c]에 visit[r] + 1값 저장

    print(f'#{test_case} {result}')                     # 결과 값 출력