# Baekjoon Online Judge - 호석이 두 마리 치킨

import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().split())
city = [[float("INF") for _ in range(N)] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    city[A-1][B-1] = 2
    city[B-1][A-1] = 2

for i in range(N):
    city[i][i] = 0

for k in range(N):
    for r in range(N):
        for c in range(N):
            if city[r][c] > city[r][k] + city[k][c]:
                city[r][c] = city[r][k] + city[k][c]


stores = list(itertools.combinations(range(1, N + 1), 2))
time_total = float("INF")
store_location = ""
for store in stores:
    first = store[0]
    second = store[1]
    answer = 0
    for flag in range(N):
        answer += min(city[flag][first-1], city[flag][second-1])

    if time_total > answer:
        time_total = answer
        store_location = store


print(store_location[0], store_location[1], time_total)
