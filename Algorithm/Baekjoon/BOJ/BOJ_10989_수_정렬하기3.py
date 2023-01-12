# Baekjoon Online Judge - 수 정렬하기 3

import sys

N = int(sys.stdin.readline())

number = {}
for _ in range(N):
    n = int(sys.stdin.readline())
    if n in number:
        number[n] += 1
    else:
        number[n] = 1

for num, cnt in sorted(number.items()):
    for _ in range(cnt):
        print(num)
