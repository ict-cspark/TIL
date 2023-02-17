# Baekjoon Online Judge - 근손실

import itertools

N, K = map(int, input().split())
tools = list(map(int, input().split()))

ways = list(itertools.permutations(range(N), N))

result = 0
for way in ways:
    weight = 500
    for w in way:
        weight += (tools[w] - K)
        if weight < 500:
            break
    else:
        result += 1

print(result)
