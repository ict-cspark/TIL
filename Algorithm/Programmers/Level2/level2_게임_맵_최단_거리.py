# Programmers - Level2 - 게임 맵 최단 거리


def solution(maps):
    N = len(maps)
    M = len(maps[0])

    delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    visited = [[0] * M for _ in range(N)]

    queue = [(0, 0)]
    visited[0][0] = 1

    while queue:
        r, c = queue.pop(0)
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and maps[nr][nc] == 1:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

    if visited[N - 1][M - 1] == 0:
        answer = -1
    else:
        answer = visited[N - 1][M - 1]
    return answer