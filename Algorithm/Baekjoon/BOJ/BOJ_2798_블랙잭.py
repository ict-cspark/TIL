# Baekjoon Online Judge - 블랙잭

'''
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
'''


from itertools import permutations

N, M = map(int, input().split())
number = list(map(int, input().split()))

answer = set()
for i in permutations(number, 3):
    temp = sum(i)
    if temp <= M:
        answer.add(temp)

print(max(answer))
