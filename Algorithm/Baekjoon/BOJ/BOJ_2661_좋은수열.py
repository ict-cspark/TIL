# Baekjoon Online Judge - 좋은수열


def DFS(K, num):
    for i in range(1, K//2 + 1):
        if str(num)[-i:] == str(num)[-(i*2):-i]:
            return

    if K == N:
        print(num)
        exit(0)
    else:
        for j in range(1, 4):
            answer = num * 10 + j
            DFS(K + 1, answer)


N = int(input())
DFS(0, 0)
