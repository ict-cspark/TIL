# Baekjoon Online Judge - 넴모넴모 (Easy)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
puzzles = [[0] * (M + 1) for _ in range(N + 1)]
answer = 0


def DFS(cnt):
    global answer

    if cnt == N * M:
        answer += 1
        return

    r = (cnt // M) + 1
    c = (cnt % M) + 1

    DFS(cnt + 1)
    if puzzles[r - 1][c] == 0 or puzzles[r][c - 1] == 0 or puzzles[r - 1][c - 1] == 0:
        puzzles[r][c] = 1
        DFS(cnt + 1)
        puzzles[r][c] = 0


DFS(0)
print(answer)
