# Baekjoon Online Judge - 최소비용 구하기

'''
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라.
도시의 번호는 1부터 N까지이다.
'''


import sys, heapq
input = sys.stdin.readline

INF = 987654321


def move(start):
    distance = [INF] * (N + 1)

    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start] = 0

    while queue:
        city, cost = heapq.heappop(queue)

        if distance[city] < cost:
            continue

        for cityN, costN in busInfo[city]:
            answer = costN + cost
            if distance[cityN] > answer:
                heapq.heappush(queue, (cityN, answer))
                distance[cityN] = answer

    return distance


N = int(input())
M = int(input())

busInfo = [[] for _ in range(N + 1)]

for _ in range(M):
    S, E, C = map(int, input().split())
    busInfo[S].append((E, C))

A, B = map(int, input().split())
result = move(A)

print(result[B])