# Baekjoon Online Judge - 선발 명단

import sys
input = sys.stdin.readline


def DFS(K, ability):
    global result

    if K == 11:
        result = max(result, ability)
        return

    for i in range(11):
        if visited[i]:
            continue
        else:
            if players[K][i]:
                visited[i] = 1
                DFS(K + 1, ability + players[K][i])
                visited[i] = 0


T = int(input())
for _ in range(T):
    players = [list(map(int, input().split())) for _ in range(11)]

    result = 0
    visited = [0] * 11
    DFS(0, 0)
    print(result)
