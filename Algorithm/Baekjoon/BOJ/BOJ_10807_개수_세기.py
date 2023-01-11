# Baekjoon Online Judge - 개수 세기

N = int(input())
num = list(map(int, input().split()))
T = int(input())

result = 0

for i in range(N):
    if T == num[i]:
        result += 1

print(result)