# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합

'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    my_min = sum(num)
    my_max = 0
    for j in range((N-M) + 1):
        temp = 0
        for k in range(M):
            temp += num[j + k]
        if my_min >= temp:
            my_min = temp
        if my_max <= temp:
            my_max = temp

        result = my_max - my_min
    print(f'#{i} {result}')