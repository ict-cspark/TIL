# Baekjoon Online Judge - 덩치

import sys
input = sys.stdin.readline

N = int(input())

people = []
for _ in range(N):
    person = list(map(int, input().split()))
    people.append(person)

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end=" ")
