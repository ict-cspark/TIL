# Baekjoon Online Judge - 서강근육맨

N = int(input())
PT = list(map(int, input().split()))
PT.sort()

if N % 2:
    result = PT.pop()
else:
    result = 0

for i in range(N//2):
    answer = PT[i] + PT[-(i + 1)]
    if result < answer:
        result = answer

print(result)
