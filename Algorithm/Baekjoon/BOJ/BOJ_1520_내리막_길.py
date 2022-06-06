# Baekjoon Online Judge - 내리막 길

'''
여행을 떠난 세준이는 지도를 하나 구하였다.
이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다.
한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며,
각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]


N, M = map(int, input().split())
visited = [[-1] * M for _ in range(N)]

path = []
for _ in range(N):
    temp = list(map(int, input().split()))
    path.append(temp)


def DFS(sr, sc):
    if sr == N - 1 and sc == M - 1:
        return 1

    if visited[sr][sc] != -1:
        return visited[sr][sc]
    else:
        visited[sr][sc] = 0

    for dr, dc in delta:
        nr = sr + dr
        nc = sc + dc

        if 0 <= nr < N and 0 <= nc < M:
            if path[sr][sc] > path[nr][nc]:
                visited[sr][sc] += DFS(nr, nc)

    return visited[sr][sc]

print(DFS(0, 0))
