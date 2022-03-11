# Baekjoon Online Judge - DFS와 BFS

'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.
'''

N, M, V = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]     # N + 1만큼의 0으로 채워진 2차원 배열 생성

for _ in range(M):                              # 탐색할 정점 갯수만큼 반복하여 양방향에 1을 표시
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1


visit = [0] * (N + 1)                           # 방문했는지 확인하기 위해 0으로 채워진 리스트 생성
visit[V] = 1                                    # 초기값으로 시작값 인덱스에 해당하는 리스트에 1 대입
stack = []                                      # stack을 적용하기 위해 빈 리스트 생성
result = [V]                                    # 다녀간 곳 순서대로 기록하기 위해 빈 리스트 생성
r = V                                           # 행의 초기값으로 시작값 설정
while True:             # DFS (스택)
    for c in range(1, N + 1):                   # 1부터 N까지 반복
        if arr[r][c] == 1 and visit[c] == 0:    # r과 c의 arr값이 1이고 visit[c]를 방문하지 않았을 경우
            stack.append(r)                     # stack에 해당 행의 값을 추가
            result.append(c)                    # result에 해당 열의 값을 추가
            visit[c] = 1                        # 방문흔적 남기기
            r = c                               # 다음 행을 반복하기 위해 r의 값을 c의 값으로 변경
            break                               # 반복문 종료 후 다음 행 실행
    else:
        if stack:                               # 반복문 종료 후에 stack 리스트에 값이 있을 경우 r에 stack 마지막 값 대입
            r = stack.pop()
        else:                                   # stack이 비어있을 경우 while문 종료
            break
print(*result)

visit = [0] * (N + 1)                           # 방문 리스트 생성하고 시작값의 인덱스에 값을 1로 변경
visit[V] = 1
queue = [V]                                     # 큐와 result 초기값을 시작값 설정
result = [V]
while queue:            # BFS (큐)   큐가 비어있지 않을때까지 반복문 실행
    r = queue.pop(0)    # r에 큐의 0번째 인덱스 값 꺼내와 대입
    for c in range(1, N + 1):                   # 만약 arr[r][c]의 값이 1이고 visit[c]가 0일 경우
        if arr[r][c] == 1 and visit[c] == 0:
            queue.append(c)                     # 큐에 c의값을 추가
            result.append(c)                    # result에 c의 값을 추가
            visit[c] = 1                        # visit[c]에 1을 대입
print(*result)