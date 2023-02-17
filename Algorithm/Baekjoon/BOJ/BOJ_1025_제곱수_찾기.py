# Baekjoon Online Judge - 제곱수 찾기

N, M = map(int, input().split())

numbers = []
for _ in range(N):
    number = list(map(int, input()))
    numbers.append(number)

result = -1
for r in range(N):
    for c in range(M):
        for nr in range(-N, N):
            for mc in range(-M, M):
                x, y = r, c
                num = ""
                if nr == 0 and mc == 0:
                    continue
                while 0 <= x < N and 0 <= y < M:
                    num += str(numbers[x][y])
                    answer = int(int(num)**0.5)**2
                    if answer == int(num):
                        result = max(result, int(num))
                    x += nr
                    y += mc

print(result)
