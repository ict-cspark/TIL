# Baekjoon Online Judge - 숫자 야구

import itertools

N = int(input())

numbers = list(itertools.permutations(range(1, 10), 3))
questions = []
for _ in range(N):
    question = list(map(int, input().split()))
    questions.append(question)

result = 0
for number in numbers:
    number = ("".join(map(str, number)))

    for question in questions:
        q_number = str(question[0])

        strike = 0
        ball = 0
        for i in range(3):
            for j in range(3):
                if number[i] == q_number[j]:
                    if i == j:
                        strike += 1
                    else:
                        ball += 1

        if strike != question[1] or ball != question[2]:
            break
    else:
        result += 1

print(result)
