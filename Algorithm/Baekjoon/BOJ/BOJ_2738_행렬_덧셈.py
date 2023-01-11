# Baekjoon Online Judge - 행렬 덧셈

N, M = map(int, input().split())

result = list([0] * M for _ in range(N))

for _ in range(2):
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(M):
            result[i][j] += temp[j]

for n in range(N):
    print(" ".join(map(str, result[n])))
