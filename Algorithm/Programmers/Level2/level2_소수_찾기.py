# Programmers - Level2 - 소수 찾기

import itertools


def solution(numbers):

    result = set()
    for i in range(1, len(numbers) + 1):
        temp = itertools.permutations(numbers, i)
        for j in temp:
            result.add(int("".join(j)))

    answer = 0
    for r in result:
        if r > 1:
            for idx in range(2, r):
                if not r % idx:
                    break
            else:
                answer += 1
    return answer

