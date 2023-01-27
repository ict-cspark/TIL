# Baekjoon Online Judge - 두~~부 두부 두부

N, M, K = map(int, input().split())

while K < 0:
    K += N

result = (((K - 3) % N) + M)
if result > N:
    result = result % N

print(result)