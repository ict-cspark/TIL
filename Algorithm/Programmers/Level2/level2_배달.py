# Programmers - Level2 - 배달

import heapq                        # 힙큐 import


def dijkstra(distance, adj):        # 다익스트라 알고리즘
    heap = []                       # 힙 생성
    heapq.heappush(heap, (0, 1))    # 1번 마을 거리는 0으로 설정

    while heap:                     # 힙이 있을때까지 반복문 실행
        cost, node = heapq.heappop(heap)    # 힙에서 꺼내와 cost, node에 할당
        for c, n in adj[node]:      # adj[node]에서 꺼내와 c, n 할당
            cost_sum = cost + c     # n번 마을까지의 시간 cost_sum에 저장
            if cost_sum < distance[n]:  # 현재 distance[n] 보다 시간이 적을경우
                distance[n] = cost_sum  # 값 갱신
                heapq.heappush(heap, (cost_sum, n)) # 최소시간과 마을을 힙에 추가

    return


def solution(N, road, K):
    INF = int(1e9)                  # INF 상수 설정
    distance = [INF] * (N + 1)      # 소요시간 리스트 INF 로 설정
    distance[1] = 0                 # 1번마을은 0으로 설정

    adj = [[] for _ in range(N + 1)]    # 인접리스트 생성
    for x, y, r in road:            # road에서 불러와 adj 리스트에 양방향 추가
        adj[x].append((r, y))
        adj[y].append((r, x))

    dijkstra(distance, adj)         # 다익스트라 함수 실행

    answer = 0
    for d in distance:              # 배달 가능 거리 마을 구하기
        if d <= K:
            answer += 1

    return answer                   # answer 리턴
