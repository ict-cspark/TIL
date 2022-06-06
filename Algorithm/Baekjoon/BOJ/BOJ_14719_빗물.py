# Baekjoon Online Judge - 빗물

'''
2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?
'''


H, W = map(int, input().split())
block = list(map(int, input().split()))

result = 0

for r in range(H, 0, -1):
    answer = 0
    flag = 0
    for c in block:
        if r <= c:
            flag = 1
            result += answer
            answer = 0
        elif r > c and flag == 1:
            answer += 1

print(result)