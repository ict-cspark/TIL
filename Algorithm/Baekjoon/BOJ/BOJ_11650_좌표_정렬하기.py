# Baekjoon Online Judge - 좌표 정렬하기

import sys

N = int(input())

numbers = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    numbers.append((x, y))

numbers = sorted(numbers, key=lambda x: (x[0], x[1]))

for x, y in numbers:
    print(x, y)
