# Baekjoon Online Judge - 소수 찾기

N = int(input())
number = list(map(int, input().split()))

prime = []
for num in range(2, 1001):
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        prime.append(num)

result = 0
for check in number:
    if check in prime:
        result += 1
print(result)
