# Baekjoon Online Judge - 숫자 카드 2

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

cards = {}
for n in numbers:
    if n in cards:
        cards[n] += 1
    else:
        cards[n] = 1

M = int(input())
check = list(map(int, input().split()))

for c in check:
    print(cards.get(c, 0), end=" ")
