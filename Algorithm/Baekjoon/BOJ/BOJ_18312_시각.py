# Baekjoon Online Judge - 시각

N, K = map(int, input().split())

result = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            time = str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2)
            if str(K) in time:
                result += 1

print(result)