# Baekjoon Online Judge - 전구

import sys

N, M = map(int, input().split())

lights = list(map(int, sys.stdin.readline().split()))

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        lights[b - 1] = c
    elif a == 2:
        for i in range(b - 1, c):
            lights[i] = lights[i] ^ 1
    elif a == 3:
        for i in range(b - 1, c):
            lights[i] = 0
    elif a == 4:
        for i in range(b - 1, c):
            lights[i] = 1

print(*lights)
