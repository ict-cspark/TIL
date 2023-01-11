# Baekjoon Online Judge - 과제 안 내신 분..?

result = list(range(1, 31))

for _ in range(28):
    N = int(input())
    result.remove(N)

sorted(result)
for i in range(2):
    print(result[i])