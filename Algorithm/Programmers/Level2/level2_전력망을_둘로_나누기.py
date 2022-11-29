# Programmers - Level2 - 전력망을 둘로 나누기


def BFS(v, n, graph):
    cnt = 0 
    queue = [v]                             # 큐 생성

    visited = [0 for _ in range(n + 1)]     # 방문 리스트 생성
    visited[v] = 1

    while queue:
        vq = queue.pop(0)                   # 순차적으로 팝

        for g in graph[vq]:                 # 해당 그래프 반복문 실행
            if visited[g] == 0:             # 방문한 적 없으면
                visited[g] = 1              # 방문흔적 남기고
                queue.append(g)             # 큐에 추가 후
                cnt += 1                    # cnt에 갯수 추가

    return cnt


def solution(n, wires):
    answer = 999
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:                    # 인접리스트 생성
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v1, v2 in wires:                    # 연결 끊기
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        cnt_v1 = BFS(v1, n, graph)          # BFS 실행
        cnt_v2 = BFS(v2, n, graph)

        answer = min(answer, abs(cnt_v1 - cnt_v2))  # answer와 절댓값 차 비교 후 최솟값 저장

        graph[v1].append(v2)                # 다시 연결
        graph[v2].append(v1)

    return answer                           # 결과 출력