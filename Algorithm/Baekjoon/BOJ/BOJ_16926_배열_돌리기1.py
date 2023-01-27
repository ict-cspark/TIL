# Baekjoon Online Judge - 배열 돌리기1

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = []

for _ in range(N):
    a = list(map(int, input().split()))
    arr.append(a)

for _ in range(R):
    for i in range(min(N, M)//2):
        x, y = i, i
        temp = arr[x][y]

        for j in range(i + 1, N - i):
            x = j
            arr_pre = arr[x][y]
            arr[x][y] = temp
            temp = arr_pre

        for j in range(i + 1, M - i):
            y = j
            arr_pre = arr[x][y]
            arr[x][y] = temp
            temp = arr_pre

        for j in range(N - i - 2, i - 1, -1):
            x = j
            arr_pre = arr[x][y]
            arr[x][y] = temp
            temp = arr_pre

        for j in range(M - i - 2, i - 1, -1):
            y = j
            arr_pre = arr[x][y]
            arr[x][y] = temp
            temp = arr_pre

for result in arr:
    print(*result)
