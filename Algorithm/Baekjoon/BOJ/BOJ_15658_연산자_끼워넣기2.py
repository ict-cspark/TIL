# Baekjoon Online Judge - 연산자 끼워넣기 (2)

import sys
input = sys.stdin.readline


def solution(answer, idx):
    global num_max, num_min

    if idx == (N - 1):
        num_max = max(num_max, answer)
        num_min = min(num_min, answer)
        return
    else:
        for i in range(4):
            if operations[i] != 0:
                operations[i] -= 1
                if i == 0:
                    solution(answer+numbers[idx+1], idx+1)
                elif i == 1:
                    solution(answer-numbers[idx+1], idx+1)
                elif i == 2:
                    solution(answer*numbers[idx+1], idx+1)
                else:
                    solution(int(answer/numbers[idx+1]), idx+1)
                operations[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))
num_max = -float("INF")
num_min = float("INF")

solution(numbers[0], 0)
print(num_max)
print(num_min)
