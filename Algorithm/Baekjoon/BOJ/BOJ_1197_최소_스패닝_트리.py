# Baekjoon Online Judge - 최소 스패닝 트리

'''
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.
'''


def Prim(s):
    INF = 1000001
    MST = [0] * (V + 1)
    KEY = [0] + [INF] * (V)
    KEY[s] = 0
    for _ in range(V):
        idx = 0
        min_value = INF
        for i in range(1, V + 1):
            if MST[i] == 0 and KEY[i] < min_value:
                idx = i
                min_value = KEY[i]

        MST[idx] = 1
        for n, w in adjL[idx]:
            if MST[n] == 0 and KEY[n] > w:
                KEY[n] = w

    return sum(KEY)

V, E = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(E)]

adjL = [[] for _ in range(V + 1)]

for n1, n2, w in num:
    adjL[n1].append((n2, w))
    adjL[n2].append((n1, w))

result = Prim(1)
print(result)