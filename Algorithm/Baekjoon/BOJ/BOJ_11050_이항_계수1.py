# Baekjoon Online Judge - 이항 계수 1

N, K = map(int, input().split())

E = N - K

result = 1

for i in range(N, E, -1):
    result *= i

for j in range(K, 0, -1):
    result //= j

print(result)