# Baekjoon Online Judge - 요세푸스 문제 0

N, K = map(int, input().split())

circle = list(range(1, N + 1))

result = "<"
idx = K - 1
while circle:
    idx = idx % len(circle)
    result += str(circle.pop(idx)) + ", "
    idx += K - 1

result = result[:-2] + ">"
print(result)
