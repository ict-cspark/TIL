# Baekjoon Online Judge - 달팽이

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N = int(input())
K = int(input())

tables = [[0] * N for _ in range(N)]

times = N ** 2

d = 0
x = 0
y = 0

for t in range(times, 0, -1):
    tables[x][y] = t

    dx = x + delta[d][0]
    dy = y + delta[d][1]

    if 0 <= dx < N and 0 <= dy < N and tables[dx][dy] == 0:
        x = dx
        y = dy
    else:
        d = (d + 1) % 4
        x += delta[d][0]
        y += delta[d][1]

a = 0
b = 0
for i in range(N):
    print(*tables[i])

    if K in tables[i]:
        a = i + 1
        b = tables[i].index(K) + 1

print(a, b)
