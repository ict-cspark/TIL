# Baekjoon Online Judge - 문어

N = int(input())
legs = [1, 2]

result = legs * (N//2)
if N % 2:
    result = result + [3]

print(*result)
