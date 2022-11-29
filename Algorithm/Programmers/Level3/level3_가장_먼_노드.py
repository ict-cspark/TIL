# Programmers - Level3 - 가장 먼 노드

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]              # 인접그래프 생성
    for a, b in edge:                               # edge 탐색하여 그래프에 저장
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n+1)                           # 방문 리스트 생성
    visited[1] = 1                                  # 출발지를 1로 설정
    queue = [1]                                     # 큐 생성 후 1부터 시작하기 위해 1저장
    while queue:                                    # 큐가 빌때까지 반복문 실행
        v = queue.pop(0)                            # 앞에서부터 큐의 요소를 꺼내 v에 저장
        for i in graph[v]:                          # graph[v]를 반복문을 돌면서
            if visited[i] == 0:                     # 방문한적이 없다면
                visited[i] = visited[v] + 1         # graph[v] + 1의 값을 저장
                queue.append(i)                     # 큐에 i 요소 추가

    result = max(visited)                           # visited에서 max값을 저장
    answer = 1                                      # answer에 초기값으로 1을 저장
    if result > 0:                                  # result가 0보다 클 경우에만
        answer = visited.count(result)              # result 값을 count하여 answer에 저장
    return answer