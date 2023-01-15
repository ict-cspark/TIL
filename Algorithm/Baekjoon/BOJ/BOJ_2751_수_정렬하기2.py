# Baekjoon Online Judge - 수 정렬하기 2

import sys

N = int(sys.stdin.readline())

numbers_pos = [0] * 1000001
numbers_neg = [0] * 1000001

for _ in range(N):
    num = int(sys.stdin.readline())
    if num < 0:
        numbers_neg[abs(num)] = 1
    else:
        numbers_pos[num] = 1

for i in range(1000000, 0, -1):
    if numbers_neg[i] == 0:
        continue
    else:
        print(-i)

for i in range(1000001):
    if numbers_pos[i] == 0:
        continue
    else:
        print(i)
