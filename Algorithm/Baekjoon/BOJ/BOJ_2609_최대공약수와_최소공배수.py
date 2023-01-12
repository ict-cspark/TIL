# Baekjoon Online Judge - 최대공약수와 최소공배수

N, M = map(int, input().split())
A = B = 0

if N >= M:
    A = N
    B = M
else:
    A = M
    B = N

max_num = 0
min_num = 0

for i in range(B, 0, -1):
    if A % i == 0 and B % i == 0:
        max_num = i
        break

print(max_num)
min_num = max_num * (A // max_num) * (B // max_num)
print(min_num)