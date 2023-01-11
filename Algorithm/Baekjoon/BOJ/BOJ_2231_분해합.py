# Baekjoon Online Judge - 분해합

N = int(input())
M = len(str(N)) * 10
start = N - M
if start < 1:
    start = 1

result = 0
for i in range(start, N):
    temp = int(i)
    for t in str(i):
        temp += int(t)
    if temp == N:
        result = i
        print(result)
        break
else:
    print(0)
